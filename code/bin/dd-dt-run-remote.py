#!/usr/bin/env python3
# encoding: utf-8

"""
dd-dt-run-remote.py

upload scripts and their confs to remote host and execute them

author  : stefan schablowski
contact : stefan.schablowski@desmodyne.com
created : 2018-12-24
"""


# TODO: move this script to another (tools ?) project


from argparse        import ArgumentParser
from distutils.spawn import find_executable
from json            import loads
from os              import environ
from os.path         import abspath, basename, dirname, exists, join
from sys             import exit

from fabric            import Connection
from invoke.exceptions import UnexpectedExit
from yaml              import YAMLError, safe_load


# -----------------------------------------------------------------------------
# main function

def main():
    """
    main function, script starting point
    """

    # NOTE: repo info currently isn't needed
    # if not environ.get('REPO_INFO'):
    #     print(('ERROR: environment variable REPO_INFO must be set to '
    #            'output of get-repo-info before calling this script\n'))
    #     return 1

    # https://docs.python.org/2/howto/argparse.html
    parser = ArgumentParser()
    parser.add_argument("conf_file",   help="path to configuration file")
    parser.add_argument("target_root", help="path to project root of target")
    args = parser.parse_args()

    conf_file   = args.conf_file
    target_root = args.target_root

    # https://stackoverflow.com/a/1774043
    # https://martin-thoma.com/configuration-files-in-python/#yaml
    with open(conf_file, 'r') as stream:
        try:
            conf = safe_load(stream)
        except YAMLError as exc:
            print(exc)

    return run_remote(conf, target_root)


# -----------------------------------------------------------------------------
# run script on remote host

def run_remote(conf, target_root):
    """
    upload scripts and conf files to remote host and run them

    arguments:
    conf        : dict with configuration
    target_root : absolute path to root folder of project calling this script
    """

    # TODO: error handling: validate arguments

    host_name         = conf['host_name']
    files_to_copy     = conf['files_to_copy']
    path_to_local_tmp = conf['path_to_local_tmp']

    path_to_local_tmp = join(target_root, path_to_local_tmp)

    # NOTE: repo_info currently isn't needed
    # repo_info = loads(environ.get('REPO_INFO'))
    # stage     = repo_info['stage']

    # TODO: look at conn as context:
    # https://stackoverflow.com/a/53447725 <-- does this work ?
    conn = Connection(host_name)

    # NOTE: on macOS Sierra, this fails with
    #   ValueError: unknown locale: UTF-8
    # unless LC_ALL=en_US.UTF-8 is set locally
    print('create temp folder on remote host:')
    result = conn.run('mktemp -d', hide='both')

    # NOTE: result.stdout has a trailing newline that causes put to fail with
    #   IOError: [Errno 2] No such file
    remote_tmp_dir = result.stdout.rstrip()
    print('  {0}'.format(remote_tmp_dir))

    file_list = []

    for path in files_to_copy.values():
        if isinstance(path, list):
            for name in path:
                file_list.append(basename(name))
        else:
            file_list.append(basename(path))

    print()
    print('copy files to remote host:')
    for name in file_list:
        print('  {0}'.format(name))
        conn.put(join(path_to_local_tmp, name),
                 remote=join(remote_tmp_dir, name))

    script_names = files_to_copy['script_names']
    config_file  = basename(files_to_copy['config_file'])
    exit_code    = 0

    print()
    for script_name in script_names:

        # TODO: ${script_name} should print errors to &2,
        # so they can be redirected appropriately here
        print('execute command line on remote host:')
        # NOTE: cd to temp dir so env file w/out path is found by $script_name
        exec_str = 'cd {0} && ./{1} {2} && cd - > /dev/null' \
                     .format(remote_tmp_dir, script_name, config_file)

        # TODO: 'docker pull' output is not printed as in live session
        print('  {0}:'.format(exec_str))
        try:
            conn.run(exec_str)
        except UnexpectedExit as exc:
            exit_code = 1
            break

    print()
    print('delete temp folder on remote host:')
    conn.run('rm -r ' + remote_tmp_dir, hide='both')
    print('  {0}'.format(remote_tmp_dir))
    print()

    return exit_code


if __name__ == "__main__":
    """
    Shell wrapper run when this script is called directly.
    """

    exit(main())
