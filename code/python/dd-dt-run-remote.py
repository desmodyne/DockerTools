#!/usr/bin/env python
# encoding: utf-8

"""
dd-dt-run-remote.py

upload scripts and their confs to remote host and execute them

author  : stefan schablowski
contact : stefan.schablowski@desmodyne.com
created : 2018-12-24
"""


# TODO: move this script to another project (e.g. RemoteTools ?)
# TODO: move this to ../python; requires extra effort when deploying


import argparse
import json

from os.path import abspath, basename, dirname, exists, join, realpath

# https://pypi.org/project/fabric
import fabric
# https://pypi.org/project/invoke
import invoke
# https://pypi.org/project/PyYAML
import yaml


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
    parser = argparse.ArgumentParser()
    parser.add_argument("conf", help="path to configuration file")
    args = parser.parse_args()

    conf_file = args.conf

    # https://stackoverflow.com/a/1774043
    # https://martin-thoma.com/configuration-files-in-python/#yaml
    with open(conf_file, 'r') as stream:
        try:
            conf = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            return 1

    # add path to conf file as received as cmd line arg to conf
    # so run_remote can determine the abs path to client root
    conf['path_to_conf_file'] = args.conf

    return run_remote(conf)


# -----------------------------------------------------------------------------
# run script on remote host

def run_remote(conf):
    """
    upload scripts and conf files to remote host and run them

    arguments:
    conf: dict with configuration
    """

    # TODO: error handling: validate arguments

    # TODO: do this algorithmically ?
    host_name           = conf['host_name']
    path_to_conf_file   = conf['path_to_conf_file']
    path_to_client_root = conf['path_to_client_root']
    path_to_local_tmp   = conf['path_to_local_tmp']
    script_names        = conf['script_names']

    path_to_conf_dir    = dirname(path_to_conf_file)
    path_to_client_root = realpath(join(path_to_conf_dir, path_to_client_root))
    path_to_local_tmp   = join(path_to_client_root, path_to_local_tmp)

    # NOTE: repo_info currently isn't needed
    # repo_info = json.loads(environ.get('REPO_INFO'))
    # stage     = repo_info['stage']

    # TODO: look at conn as context:
    # https://stackoverflow.com/a/53447725 <-- does this work ?
    conn = fabric.Connection(host_name)

    # NOTE: on macOS Sierra, this fails with
    #   ValueError: unknown locale: UTF-8
    # unless LC_ALL=en_US.UTF-8 is set locally
    print('create temp folder on remote host:')
    result = conn.run('mktemp -d', hide='both')

    # NOTE: result.stdout has a trailing newline that causes put to fail with
    #   IOError: [Errno 2] No such file
    remote_tmp_dir = result.stdout.rstrip()
    print(f'  {remote_tmp_dir}')

    file_list = []

    # NOTE: convention on file names (template not used here):
    #  1. configuration file name = <script name>.yaml
    #  2. conf template file name = <script name>.yaml.j2

    # for every script, add its conf file to list
    for script_name in script_names:
        conf_file = f'{script_name}.yaml'
        file_list.append(conf_file)

    # sort list for better readable log output
    file_list.sort()

    print()
    print('copy files to remote host:')
    for name in file_list:
        print(f'  {name}')
        conn.put(join(path_to_local_tmp, name),
                 remote=join(remote_tmp_dir, name))

    exit_code = 0

    print()
    for script_name in script_names:
        conf_file = f'{script_name}.yaml'

        # TODO: ${script_name} should print errors to &2,
        # so they can be redirected appropriately here
        print('execute command line on remote host:')
        # NOTE: cd to temp dir so env file w/out path is found by $script_name
        exec_str = f'{script_name} {remote_tmp_dir}/{conf_file}'

        # TODO: 'docker pull' output is not printed as in live session
        print(f'  {exec_str}:')
        try:
            conn.run(exec_str)
        except invoke.exceptions.UnexpectedExit as exc:
            exit_code = 1
            break

    print('delete temp folder on remote host:')
    conn.run(f'rm -r {remote_tmp_dir}', hide='both')
    print(f'  {remote_tmp_dir}')
    print()

    return exit_code


# -----------------------------------------------------------------------------
# shell wrapper

if __name__ == "__main__":
    """
    Shell wrapper run when this script is called directly.
    """

    import sys

    # TODO: pass all command line arguments ?
    # not currently required with ArgumentParser...
    sys.exit(main())
