    commit 408b5c6b767d5248feeba7f77d6ce0c7348c94a8
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Sep 24 16:48:41 2019 +0300
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Sep 24 16:48:41 2019 +0300
    
        [#1]: update project version to 0.0.4
    
    commit 6faa569329fb2e1034e1377b16d7524bdc93ffc0
    Merge: 21821be ff19a53
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Sep 24 13:48:00 2019 +0000
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Sep 24 13:48:00 2019 +0000
    
        Merge branch 'feature/3/use_in_production_and_improve' into 'develop'
        
        Feature/3/use in production and improve
        
        See merge request DesmoDyne/Tools/DockerTools!8
    
    commit ff19a538ebbb1914d07b655f8a2ce9a381ed154b
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Sep 24 16:25:31 2019 +0300
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Sep 24 16:47:18 2019 +0300
    
        [#3]: add dt- to script names to align with corp conv; done with
        
        $ mapfile -t filenames < <(ls)
        $ for file in "${filenames[@]}"
          do
            for filename in "${filenames[@]}"
            do
              sed_expr="s|${filename}|$(sed -e 's|dd-|dd-dt-|g' ...
               ... <<< "${filename}")|g"
              gsed -i -e "${sed_expr}" "${file}"
            done
            mv "${file}" "$(sed -e 's|dd-|dd-dt-|g' <<< "${file}")"
          done
    
    commit 4e4e719f9eddd64495f70834a9a6aa45554fb0f5
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Sep 24 16:12:37 2019 +0300
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Sep 24 16:47:18 2019 +0300
    
        [#3]: review shellcheck issues
    
    commit a32cd879752104d7f6ce5c6a4fb545865ebc96be
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Sep 24 15:29:44 2019 +0300
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Sep 24 16:47:18 2019 +0300
    
        [#3]: align file permissions
    
    commit ded242b84e980f2e9c88da67db0adccdd632b639
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Sep 24 15:24:19 2019 +0300
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Sep 24 16:47:18 2019 +0300
    
        [#3]: add shell wrapper script to run dd-run-remote.py in pipenv venv
    
    commit 92d9a65ab16cfed6f0be08fe750f4eb7f4d57003
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Sep 24 14:48:41 2019 +0300
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Sep 24 16:47:18 2019 +0300
    
        [#3]: append .py to script name to make room for shell wrapper; review
    
    commit bd179ab0dd483dc21ebc2befbdf9c862f7fc505d
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Sep 24 14:42:45 2019 +0300
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Sep 24 16:47:18 2019 +0300
    
        [#3]: git-ignore .../.venv with easily reproducible pipenv venv files
    
    commit 5e9823976eba1915b11743d26b507b46eec10925
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Sep 24 14:32:58 2019 +0300
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Sep 24 16:47:18 2019 +0300
    
        [#3]: introduce pipenv to the project and create venv for dd-run-remote:
        
        following http://docs.pipenv.org/en/latest/install:
        
        + add these lines to ~/.bash_profile:
        export PATH="${HOME}/Library/Python/2.7/bin":$PATH
        export PATH="${HOME}/Library/Python/3.7/bin":$PATH
        export PIPENV_VENV_IN_PROJECT=1
        
        $ brew install pipenv
           ...
        $ pip install --user pipenv
           ...
        
        $ pwd
        /Users/ssc/DevBase/DesmoDyne/Tools/DockerTools
        
        alexa:DockerTools ssc$ pipenv install fabric pyyaml
        Creating a virtualenv for this project…
        Pipfile: /Users/ssc/DevBase/DesmoDyne/Tools/DockerTools/Pipfile
        Using /usr/local/opt/python/bin/python3.7 (3.7.4) to create virtualenv…
        ⠧ Creating virtual environment...
        Already using interpreter /usr/local/opt/python/bin/python3.7
        Using base prefix '/usr/local/Cellar/python/3.7.4_1/Frameworks/ ...
                            ... Python.framework/Versions/3.7'
        New python executable in /Users/ssc/DevBase/DesmoDyne/Tools/ ...
                                  ... DockerTools/.venv/bin/python3.7
        Also creating executable in /Users/ssc/DevBase/DesmoDyne/Tools/ ...
                                     ... DockerTools/.venv/bin/python
        Installing setuptools, pip, wheel...
        done.
        
        ✔ Successfully created virtual environment!
        Virtualenv location:
          /Users/ssc/DevBase/DesmoDyne/Tools/DockerTools/.venv
        Creating a Pipfile for this project…
        Installing fabric…
        Adding fabric to Pipfile's [packages]…
        ✔ Installation Succeeded
        Installing pyyaml…
        Adding pyyaml to Pipfile's [packages]…
        ✔ Installation Succeeded
        Pipfile.lock not found, creating…
        Locking [dev-packages] dependencies…
        Locking [packages] dependencies…
        ✔ Success!
        Updated Pipfile.lock (fc8d70)!
        Installing dependencies from Pipfile.lock (fc8d70)…
          🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 11/11 — 00:00:03
        To activate this project's virtualenv, run pipenv shell.
        Alternatively, run a command inside the virtualenv with pipenv run.
    
    commit 1a65941c34f905e0e2d7275ef97bf6a69c927827
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Sep 24 13:41:57 2019 +0300
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Sep 24 16:47:18 2019 +0300
    
        [#3]: use python3 instead of python2
    
    commit 24d65525db5950bd8e77214192b6f9cb1c3dad47
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Sep 24 13:15:21 2019 +0300
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Sep 24 16:47:18 2019 +0300
    
        [#3]: review shellcheck issues
    
    commit 127f5c04b92f0df88f28d5974efabaae5289f4af
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Sep 24 12:40:42 2019 +0300
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Sep 24 16:47:18 2019 +0300
    
        [#3]: copy and adapt gitlab CI/CD conf from BashLib project;
        
        taken from
          https://gitlab.com/DesmoDyne/Tools/BashLib/tree/develop
        at commit
          https://gitlab.com/DesmoDyne/Tools/BashLib/commit/ ...
           ... 66456587796d3e0eae4aa5b8d9cf996664a15711
    
    commit a5098b8d6260d0d48be29f216142005d55a3b649
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Sep 24 12:39:56 2019 +0300
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Sep 24 16:47:18 2019 +0300
    
        [#3]: copy and adapt CI/CD scripts and conf from BashLib project;
        
        taken from
          https://gitlab.com/DesmoDyne/Tools/BashLib/tree/develop
        at commit
          https://gitlab.com/DesmoDyne/Tools/BashLib/commit/ ...
           ... 66456587796d3e0eae4aa5b8d9cf996664a15711
    
    commit 94e2a61dc9fafe237c41bb69674ebc954a29be4b
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Sep 24 12:37:44 2019 +0300
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Sep 24 16:47:18 2019 +0300
    
        [#3]: add brew formula template derived from live file for version 0.0.3
    
    commit 19777fdbd495d24c421b38df2f63bef29395631f
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Sep 24 12:35:31 2019 +0300
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Sep 24 12:35:31 2019 +0300
    
        [#3]: update conf file in project to convention in latest ReleaseTools
    
    commit a79e7e3f9294f4052e33434d561b11ac520102a9
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Sep 24 12:13:50 2019 +0300
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Sep 24 12:13:50 2019 +0300
    
        [#3]: align code for getting conf from file to using BashLib function
    
    commit f503ea2ae6ca515968bd001026c768da0aa4660d
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Sep 24 11:19:27 2019 +0300
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Sep 24 11:19:27 2019 +0300
    
        [#3]: align code to load BashLib with convention; same change many times
    
    commit 78a9f25a9837ad508e1d52ea7f3707cbff8199a9
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Fri Sep 20 17:53:08 2019 +0300
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Fri Sep 20 17:53:08 2019 +0300
    
        [#3]: do not test for REPO_INFO env var; not used currently
    
    commit 154ef480058cf59f3c18c094ca0b4598059473a9
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Thu Aug 22 20:32:46 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Thu Aug 22 20:32:46 2019 +0200
    
        [#3]: add simple utility script to list docker networks
    
    commit 7c2c481e8ef64b47091e90ace3e1d88eec02a538
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Thu Aug 22 19:19:12 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Thu Aug 22 19:19:12 2019 +0200
    
        [#3]: store secrets obtained from vault as single temporary json file
    
    commit f0b6b47073fc837dfe00099df3d6de7d65dfbb9f
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Thu Aug 22 15:46:13 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Thu Aug 22 15:46:13 2019 +0200
    
        [#3]: get configured secrets from public vault instance; not used yet
    
    commit 51f8e8aaf9595cdbcd8390edd762321af71fc06b
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Thu Aug 22 12:39:21 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Thu Aug 22 12:39:21 2019 +0200
    
        [#3]: use array instead of setting IFS when copying secrets files
    
    commit 0a6beaa28070eade0b19ed1744331e9fc9316215
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Thu Aug 22 11:16:54 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Thu Aug 22 11:16:54 2019 +0200
    
        [#3]: improve error handling and log output when copying secrets files
    
    commit 4728f3ddd4357226ac5d13bc77e13e6b81e2ae5d
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Wed Jul 31 20:13:42 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Wed Jul 31 20:13:42 2019 +0200
    
        [#3]: use per-image temp backup folder to scale for multiple image confs
    
    commit 9207b01ad5f0652f1f6f096ddc68edc7a4fcce0d
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Wed Jul 31 10:02:12 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Wed Jul 31 10:02:12 2019 +0200
    
        [#3]: rename backup_cont_image_name variable name to make it shorter
    
    commit fb93ead67d7619e0dbec2dd6ac26ffcaf188667d
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Wed Jul 10 10:37:57 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Jul 30 10:37:48 2019 +0200
    
        [#3]: try to upload second tag first to fail immediately if not present
    
    commit 107cd9bac34c85941f5abf70bbffefced1925a5f
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Mon Jul 8 12:13:02 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Jul 30 10:37:48 2019 +0200
    
        [#3]: use .../tmp/deploy/backup instead of /tmp/deploy/backup
    
    commit 5f00eb969d05ecbd9bca7bf35bcbf882b3d84133
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Jul 7 21:51:31 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Jul 30 10:37:48 2019 +0200
    
        [#3]: add utility scripts to list containers, images and volumes sorted
    
    commit 2661647570185d2857d5905c37d1bb95dbcaac55
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Jul 7 15:03:00 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Jul 30 10:37:48 2019 +0200
    
        [#3]: align: get mandatory and optional attributes from image conf;
        
        add build-args to 'docker build' arguments; display full docker cmd line
    
    commit c45596dc4d8b4429b6604f7977413d00b6486685
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Jul 7 12:06:09 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Jul 7 21:52:03 2019 +0200
    
        [#3]: add TODO comment on warnings displayed by 'docker login'
    
    commit 9138e304f7978260bb377bfe24065caab2fc569a
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Jul 7 12:04:18 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Jul 7 21:52:03 2019 +0200
    
        [#3]: get env file name not path from conf and cd to temp folder
    
    commit 2b3ca5153d794eba4b5b0a479d57fded9145715f
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Jul 7 10:10:16 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Jul 7 21:52:03 2019 +0200
    
        [#3]: get env file path from conf and add to docker run arguments
    
    commit 1c14d829eb9bc291d47a5dfcb3d3a4286c6aca20
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Jul 7 10:09:19 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Jul 7 21:52:03 2019 +0200
    
        [#3]: return with error code if script failed; simplify script execution
    
    commit ffa12fb1edcf8ed091f940ae9967447dd4d4de74
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sat Jul 6 18:10:46 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Jul 7 21:52:03 2019 +0200
    
        [#3]: get both stage and second image tags from conf, use second tag
    
    commit 713cf129357ec25ef4473db9115d892d816a185b
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sat Jul 6 18:04:44 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Jul 7 21:52:03 2019 +0200
    
        [#3]: change image_tag_commit to more generic image_tag_second:
        
        the tag contains a semver, not a commit hash, for release and master
    
    commit 9a79e561d9ab35466bcd158ef7b197de276b4252
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sat Jul 6 17:46:32 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Jul 7 21:52:03 2019 +0200
    
        [#3]: remove code to render template that is no longer needed
    
    commit 0303a050bc63cab6290133d667e24a354b02aaf6
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Fri Jul 5 11:53:14 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sat Jul 6 17:49:00 2019 +0200
    
        [#3]: push image with both stage and commit/semver tags
    
    commit 32516ea5f861ad7328f487bc836cd46c7131cdef
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Fri Jul 5 10:04:10 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Fri Jul 5 11:53:30 2019 +0200
    
        [#3]: tag image with both stage and commit / semver
    
    commit 89b43dac75d7689d0ba17fa1e38a6fc88a8eb61c
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Fri Jun 28 21:32:26 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Fri Jul 5 11:53:30 2019 +0200
    
        [#3]: use docker login creds provided by CI when running in CI context
    
    commit 8d3cd59bcb096ed093c97d64cb5bc2059059c6d9
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Fri Jun 28 15:58:36 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Fri Jun 28 15:58:36 2019 +0200
    
        [#3]: begin to support getting optional attributes from configuration
    
    commit 9672302b0cab05c61271ac4742ae428f00d3b014
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Jun 16 19:04:27 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Jun 16 19:04:27 2019 +0200
    
        [#3]: get repo info from environment variable; render conf from template
    
    commit e00b15448be251c6a4b2e5b8866464adeaf2d6d3
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Jun 16 17:59:17 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Jun 16 17:59:17 2019 +0200
    
        [#3]: pass path to target project root as parameter; use relative tmp
    
    commit c6bc6cd77f46470149a60ab57b2ea83ba7b46fa9
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Jun 16 17:55:19 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Jun 16 17:55:19 2019 +0200
    
        [#3]: align loading script conf and variable names with convention
    
    commit 21821be7e4139e8929e9d887c6381bff77eaae26
    Merge: b74c23e 751cd06
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Thu Jun 13 12:25:16 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Thu Jun 13 12:25:16 2019 +0200
    
        Merge tag '0.0.3' into develop
        
        automatically_created_release_tag 0.0.3
