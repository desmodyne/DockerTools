    commit cd277dcc275847910a5b40d550c7a313debbd9db
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sat Sep 12 11:53:52 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sat Sep 12 11:53:52 2020 +0200
    
        [#1]: update project version to 0.0.6
    
    commit eae5d60f527bc4923d39094a6c2226dd6a0db742
    Merge: 6caceee a6e0846
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sat Sep 12 09:53:02 2020 +0000
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sat Sep 12 09:53:02 2020 +0000
    
        Merge branch 'feature/4/refactor_configuration_concept' into 'develop'
        
        Feature/4/refactor configuration concept
        
        See merge request DesmoDyne/Tools/DockerTools!14
    
    commit a6e0846d6c79b1be9427456ef8ff860f767ec99b
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sat Sep 12 11:48:32 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sat Sep 12 11:48:32 2020 +0200
    
        [#4]: in production environment, call python script without pipenv
    
    commit a3426ab1182230cc2b72408e3391468a0576f99e
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sat Sep 12 11:46:35 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sat Sep 12 11:46:35 2020 +0200
    
        [#4]: install python scripts not using pipenv but as per homebrew conv
    
    commit 48f979a0eef797c9866d6c1d9570da74c5e449ab
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sat Sep 12 09:26:00 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sat Sep 12 09:26:00 2020 +0200
    
        [#4]: remove support for obsolete PATH_TO_SECRETS build arg
    
    commit 6cdc3dd885f64d9bff29477de56247289cbf31ff
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Fri Sep 11 14:18:08 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Fri Sep 11 14:18:08 2020 +0200
    
        [#4]: work around permission denied issue when creating Python venv
    
    commit df8f9ffe6fbc2032ff8cc8731e66f2b9c5c82b53
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Mon Aug 24 18:55:09 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Mon Aug 24 18:55:09 2020 +0200
    
        [#4]: add / improve error handling; add / fix log messages
    
    commit e743f899214320a47fc43c09ec04b612ac2288c1
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Aug 9 23:26:10 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Aug 9 23:38:50 2020 +0200
    
        [#4]: also install python script and Pipfile* ${HOMEBREW_PREFIX}/bin :-/
    
    commit 5b1379de8eb9cd738459a9224c030bb7558fb836
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Aug 9 23:15:49 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Aug 9 23:38:50 2020 +0200
    
        [#4]: get environment, find python script in folder dep on dev/prod
    
    commit 7feeef0fea557c2de68736c2be42fb59e4ef1a16
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Aug 9 23:14:27 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Aug 9 23:18:38 2020 +0200
    
        [#4]: update Python to 3.8
    
    commit 70801b6b17ce608cdd0699965096933166024c63
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Aug 9 23:13:51 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Aug 9 23:18:38 2020 +0200
    
        [#4]: align upload script/conf with RepoTools; remove obs script/conf;
        
        review brew formula template, align location with conv
    
    commit 343de3e05878724e933b7b99b7fd38958e7a2c2c
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Aug 9 22:19:49 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Aug 9 22:55:27 2020 +0200
    
        [#4]: align meta files with conv at RepoTools; review TODO; del old doc
    
    commit 4277c0b1bf00e996f6d6a414f06b17963081ab17
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Wed Jul 8 16:20:27 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Wed Jul 8 16:20:27 2020 +0200
    
        [#4]: support more than one build arg
    
    commit e216e893f0bb84bc27fca7cda68af19666a7e4d8
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Jul 7 14:41:41 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Jul 7 14:41:41 2020 +0200
    
        [#4]: fix getting latest image tag for DIRTY images
    
    commit eb372a007a394ca6bba534789be88a7c737c596d
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Jul 7 14:40:46 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Jul 7 14:40:46 2020 +0200
    
        [#4]: fix setting latest image tag for DIRTY images
    
    commit 7e1768a03c3ffc5336bd9d5d42d53c19082effc9
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Thu Jul 2 22:23:19 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Thu Jul 2 22:23:19 2020 +0200
    
        [#4]: fix template: ensure it works if no volumes are configured
    
    commit 760ecdc82a103df0acbab3a1947a274e08034e26
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Thu Jul 2 20:14:49 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Thu Jul 2 20:14:49 2020 +0200
    
        [#4]: fix script: ensure it works if no vault paths are configured
    
    commit 4115b2576a8770b4da8bdc4b472fe2a26b37733c
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Thu Jul 2 19:30:33 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Thu Jul 2 19:30:33 2020 +0200
    
        [#4]: fix template: ensure it works if no vault paths are configured
    
    commit da131e2604acc24859ce7610082d6a51a82448bc
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Thu Jul 2 09:41:44 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Thu Jul 2 09:41:44 2020 +0200
    
        [#4]: do not add latest tag when building build images
    
    commit af3aedd562bea76778b91c011e39a1a24b52ec42
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Wed Jul 1 18:46:23 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Thu Jul 2 07:20:19 2020 +0200
    
        [#4]: add additional <stage>-latest tag to all built images
    
    commit b7942dd9e843aaa8eb823b0a2f0eb4cb7fa6ab65
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Mon Jun 29 08:11:01 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Thu Jul 2 07:20:19 2020 +0200
    
        [#4]: use start/end strings from BashLib; align with conv; add TODOs
    
    commit c531074add2eb9cc98ca9154a9a329937d08419c
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sat Jun 27 13:41:12 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sat Jun 27 13:41:12 2020 +0200
    
        [#4]: use role ID and secret ID from conf instead of root token to auth;
        
        + save secrets obtained from vault into per-path file, not one big one
        + pass path to secrets to docker when building container
        + add a copy of check_vault_response, taken from VaultTools > vault lib
        + adapt to conv agreed with MailFlow Database on rel/abs temp paths
    
    commit 9cd31661b9428c6c4103dcee7c6ca00b3666ef4d
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Thu Jun 25 08:46:51 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Thu Jun 25 08:47:04 2020 +0200
    
        [#4]: refactor to using a single compound vault configuration;
        
        TODO: get role ID / secret ID from conf instead of using root token
    
    commit b8ed9e4eb2cc28166248720db444a68f71ddfcba
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Jun 23 16:30:48 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Jun 23 17:51:33 2020 +0200
    
        [#4]: do not create path to secrets: must be done by client project
    
    commit ee54ba0be017bd711c5a026395533a438da5f684
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Jun 23 16:14:32 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Jun 23 16:30:13 2020 +0200
    
        [#4]: remove secrets_files: was used to copy files from local sec loc;
        
        this is not done in any relevant current projects anymore; instead, get
        all secrets from vault.desmodyne.dev in any current and future projects;
        somewhat relevant secret_files occurrences in code or conf:
        $ ack --ignore-dir=attic --sort-files secrets_files ~/DevBase/DesmoDyne
        --> ... Infrastructure/Services/CRM & ERP/odoo
        --> ... Infrastructure/Services/File Server/NextCloud
    
    commit f4501c06d8c9d74679640cf84198b353d2e07460
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Mon Jun 22 19:31:51 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Mon Jun 22 19:31:51 2020 +0200
    
        [#4]: deal with empty list of files to copy
    
    commit 5102696038f3c3d066503410c9668ce5cbc835fb
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Mon Jun 22 13:37:43 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Mon Jun 22 13:37:43 2020 +0200
    
        [#4]: run docker image prune --force to remove unused images
    
    commit e896cf1f54035bc593da3157a506b94b388df1b8
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Mon Jun 22 12:43:41 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Mon Jun 22 12:43:41 2020 +0200
    
        [#4]: run docker-compose pull to ensure latest images are used
    
    commit d84241bb93536f1a3b2faef94b7ff3a141eb51d7
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Mon Jun 22 12:31:52 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Mon Jun 22 12:31:52 2020 +0200
    
        [#4]: remove volumes when bringing down a container composition
    
    commit 4e785286a54940ab3ba8540b0dc4be8df066a041
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Mon Jun 22 11:33:45 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Mon Jun 22 12:20:59 2020 +0200
    
        [#4]: move helper scripts in here to make them more widely available;
        
        align with conv introduced in RepoTools / get-repo-info
        
        taken from
          https://gitlab.com/DesmoDyne/Infrastructure/Services/-/ ...
           ... tree/feature/119/set_up_vault.desmodyne.dev/ ...
           ... InfoSec/HashiCorp%20Vault/cicd/bin
        at commit
          https://gitlab.com/DesmoDyne/Infrastructure/Services/-/ ...
           ... commit/6c9d82f40080c1616bc7fca8fd88ca58257a99eb
    
    commit 1ca9990086c6c1d25b3324224b86ce9f88d7a4f9
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Mon Jun 22 07:55:47 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Mon Jun 22 07:55:47 2020 +0200
    
        [#4]: add TODO on path_to_secrets; not currently used --> review later
    
    commit c2f3d540807da20b8b4313ed10708dac212b043e
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Mon Jun 22 07:09:48 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Mon Jun 22 07:27:56 2020 +0200
    
        [#4]: set project name to ensure containers are stopped properly
    
    commit 3420a647eb933058b7616b8a338d9f7f87d53e5b
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Jun 21 23:05:55 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Jun 21 23:09:27 2020 +0200
    
        [#4]: find <stage>-latest image tag; upload if it exists, warn if not
    
    commit 257c12b8a0f9c3d712199ad0ab3d374e9b8036b6
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Jun 21 21:43:19 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Jun 21 23:09:27 2020 +0200
    
        [#4]: review TODOs
    
    commit d2ec6eec3e9d4f7a42ae7120475c7b18dcd91b2e
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Jun 21 21:43:04 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Jun 21 23:09:27 2020 +0200
    
        [#4]: log into gitlab container registry to download private images
    
    commit 6a7fbca0a8f9527126f12b8ff1020519d60d8f38
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Jun 21 20:58:48 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Jun 21 20:58:48 2020 +0200
    
        [#4]: align code and log output with conv; review required tools
    
    commit cf563aef04bdfc8d4108de1d3b5d9b9f34838529
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Jun 21 20:58:10 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Jun 21 20:58:10 2020 +0200
    
        [#4]: add support for files to copy; use fabric cd context
    
    commit 5bcef4d81996cf6fabd3ab5987af6306d3d441b1
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Jun 21 20:55:51 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Jun 21 20:55:51 2020 +0200
    
        [#4]: resurrect and adapt script to run cont comp; align with conv
    
    commit b57186adced37c76f57e2123961c3aebc0719b6f
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sat Jun 20 15:31:45 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sat Jun 20 15:31:45 2020 +0200
    
        [#5]: get username and password from gitlab_reg_creds compound tmpl attr
    
    commit 18c52238ab684905169c93edab595a9aca79b43a
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Thu Jun 18 16:53:21 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Thu Jun 18 16:53:21 2020 +0200
    
        [#4]: move currently ununsed, non-conv conforming scripts to attic
    
    commit 93076fe28ded3f46ebe351403dcc524cc3bb0f09
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Thu Jun 18 14:22:04 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Thu Jun 18 15:14:41 2020 +0200
    
        [#4]: delete configured container volumes if they exist; review output
    
    commit 03ea28174af86ae9090be9528eb941b12ae29dd9
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Thu Jun 18 13:40:42 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Thu Jun 18 15:14:41 2020 +0200
    
        [#4]: doc conf props conv; align handling of optional attrs in templates
    
    commit caedf6f42ef925f9f258fe357d282952196b9a60
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Wed Jun 17 19:16:20 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Thu Jun 18 10:25:56 2020 +0200
    
        [#4]: use optional conf props in template only if they were passed
    
    commit 319386ee824c30a592cada76f48794c817d82537
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Wed Jun 17 17:15:27 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Thu Jun 18 10:25:56 2020 +0200
    
        [#4]: align variable names: use vault_address, not vault_host
    
    commit bc91031c707fa2d46ec0cf8f90931c6d25e2a4ad
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Jun 16 14:02:34 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Thu Jun 18 10:25:56 2020 +0200
    
        [#4]: align code with conv; get scripts to work
    
    commit dfa671b6a140721492c87b63862b7d5551360b23
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Jun 16 12:40:05 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Jun 16 12:40:05 2020 +0200
    
        [#4]: $ pipenv install fabric pyyaml
        
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
          🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 10/10 — 00:00:01
        To activate this project's virtualenv, run pipenv shell.
        Alternatively, run a command inside the virtualenv with pipenv run.
    
    commit cef81b122e61e9342271c97c00b363d7e1ab1b0e
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Jun 16 12:39:08 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Jun 16 12:39:08 2020 +0200
    
        [#4]: remove Pipfiles at project root, don't belong there
    
    commit 925348432cd3314b0dfaf955a4073b4d2d58b6bc
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Jun 16 12:35:07 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Jun 16 12:35:07 2020 +0200
    
        [#4]: move python script to code/python; begin to review parameters
    
    commit 289d54f5ee214f2ca9e3e85f4659541f98ebacda
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Jun 16 12:11:40 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Jun 16 12:11:59 2020 +0200
    
        [#4]: begin to get script to work: tmpl work, need to commit to move
    
    commit 2135f7d39f9b85ec54912a34151d3c0b72520904
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Jun 16 12:08:10 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Jun 16 12:11:59 2020 +0200
    
        [#4]: align yaml style: do not indent lists, not necessary
    
    commit 0309eb32f75abea71b13b58039754bd8c9debc17
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Jun 16 10:18:23 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Jun 16 12:11:59 2020 +0200
    
        [#4]: remove unneeded conf prop; add TODOs; comment on macOS Keychain
    
    commit 62e81018350ca3ca83caf04b7ef34b28ea77abd3
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Mon Jun 15 08:04:49 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Jun 16 12:11:59 2020 +0200
    
        [#4]: set network name and volumes only if passed in template data
    
    commit 4721363919312203bcd37a2b131e96cb389f6055
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Mon Jun 15 08:04:09 2020 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Jun 16 12:11:59 2020 +0200
    
        [#4]: micro cross-project code / comment alignments with conventions
    
    commit 6caceee7a6c42c0a5206075d5988b70c99009b31
    Merge: c68d76e e4d50e9
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Wed Feb 19 12:26:24 2020 +0000
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Wed Feb 19 12:26:24 2020 +0000
    
        Merge branch 'feature/4/refactor_configuration_concept' into 'develop'
        
        [#4]: add support for Docker network name to run container in
        
        See merge request DesmoDyne/Tools/DockerTools!12
    
    commit e4d50e980af3b8fed4bd2f2622bbe3f41005209a
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Wed Feb 19 13:01:10 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Wed Feb 19 13:01:10 2020 +0100
    
        [#4]: add support for Docker network name to run container in
    
    commit c68d76efaa690808cfa5c7686943b057d187af6e
    Merge: 68f04ff a9a7817
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Wed Feb 19 11:20:18 2020 +0000
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Wed Feb 19 11:20:18 2020 +0000
    
        Merge branch 'feature/4/refactor_configuration_concept' into 'develop'
        
        Feature/4/refactor configuration concept
        
        See merge request DesmoDyne/Tools/DockerTools!11
    
    commit a9a7817badb49f30397663f885aec8c0eccc9c28
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Wed Feb 19 11:26:12 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Wed Feb 19 11:39:01 2020 +0100
    
        [#4]: test if lists are defined before attempting to iterate over them
    
    commit 7e11d030e2824e2fcb85d2af112f7601634d5ec8
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Wed Feb 19 09:47:33 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Wed Feb 19 09:47:33 2020 +0100
    
        [#4]: add TODO comment
    
    commit e19b777015e21f56f8808d5592dc362f337363e2
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Wed Feb 19 09:33:05 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Wed Feb 19 09:33:05 2020 +0100
    
        [#4]: work around jinja2 outputting None if template value is null
    
    commit 1e835eb88817a5005abcd86247b17af9b040f144
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Feb 18 19:35:46 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Feb 18 19:55:57 2020 +0100
    
        [#4]: rename script to reflect reduction to one single container image;
        
        update file header and log output; add TODO comment
    
    commit 7bed719bc65a12f11f129742a44d9d770b116841
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Feb 18 19:35:24 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Feb 18 19:36:03 2020 +0100
    
        [#4]: for every script to use on remote, add its conf file to list
    
    commit d4deb2f9265ef5d66bfbe6d8419274fa56df86da
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Feb 18 19:33:54 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Feb 18 19:36:03 2020 +0100
    
        [#4]: refactor script as before, work on one single cont image conf only
    
    commit 3a612ef64de4dc8a159e5e80b9d95bfd2858b817
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Feb 18 19:32:08 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Feb 18 19:36:03 2020 +0100
    
        [#4]: refactor copied conf file as before
    
    commit 60a71d1de6ba11b4fc1de8eacfe5241f58c31ba2
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Feb 18 17:52:32 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Feb 18 17:52:32 2020 +0100
    
        [#4]: copy MailFlow Database > .../cicd/conf/feature/deploy.yaml
    
    commit 4ce7d4f5dd45a728126aa7a405c06edb1b5e91be
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Feb 18 15:52:08 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Feb 18 15:52:08 2020 +0100
    
        [#4]: employ convention: derive script conf file name from script name
    
    commit 26511b342ec405f5689b03030912b75b151e2bd9
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Feb 18 13:37:46 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Feb 18 15:22:31 2020 +0100
    
        [#4]: refactor copied conf file as before:
        
        + update header
        + remove attributes not used by by code/bin/dd-dt-run-remote(.py)
        + replace hardcoded values by template variables
        + image configurations are not used, so nothing to reduce to
    
    commit 386639aabbb79cb93d8024d43f26c6e01fd89fa7
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Feb 18 13:18:44 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Feb 18 13:18:44 2020 +0100
    
        [#4]: copy MailFlow Database > .../cicd/conf/feature/deploy.yaml
    
    commit 7d4af225de2ba6be9d6689d21b8a376220a1f759
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Feb 18 12:42:50 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Feb 18 12:42:50 2020 +0100
    
        [#4]: rename script to reflect reduction to one single container image
    
    commit e0ae058991440cf5870144988c5972b42432d6ac
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Feb 18 12:40:56 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Feb 18 12:42:29 2020 +0100
    
        [#4]: refactor script and its conf as for build and dev scripts before
    
    commit 0b9676d1fa0e2ff72fae67d7c37f5f259bf3ff21
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Feb 18 09:47:19 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Feb 18 09:47:19 2020 +0100
    
        [#4]: copy MailFlow Database > .../cicd/conf/feature/upload.yaml
    
    commit 32e518174efa3fe57c0d6bb0a77006e13689aaba
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Feb 18 09:37:46 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Feb 18 09:38:08 2020 +0100
    
        [#4]: add configuration templates to brew package installation
    
    commit 84e296902f89c55a8e6ddfb75b25b72f13218f97
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Feb 18 09:25:19 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Feb 18 09:38:08 2020 +0100
    
        [#4]: support production context for use on contabo CI/CD machine
    
    commit a82871e1629b8b9182ad8cede1d7bc8587912b07
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Mon Feb 17 18:11:51 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Mon Feb 17 18:13:53 2020 +0100
    
        [#4]: rename script to reflect reduction to one single container image
    
    commit d006e8db77a2bef22188514083b4925847fe7283
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Mon Feb 17 18:00:37 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Mon Feb 17 18:13:53 2020 +0100
    
        [#4]: use client root instead of project root to reduce confusion
    
    commit d809db6158864064e3bf2bed0a9c816b5fc89065
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Mon Feb 17 16:41:56 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Mon Feb 17 18:13:53 2020 +0100
    
        [#4]: reduce to working on one single container image configuration only
    
    commit 06b3378f1740856652c1c9b64f1f541b6d04862f
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Mon Feb 17 14:57:08 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Mon Feb 17 14:57:08 2020 +0100
    
        [#4]: update header; remove attributes not used by DockerTools script;
        
        reduce to  one single image conf; replace hardcoded values by tmpl vars
    
    commit 47c9be9d226ce0904650ee6eff57c37c899cf4dc
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Mon Feb 17 14:38:18 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Mon Feb 17 14:38:18 2020 +0100
    
        [#4]: copy MailFlow Database > .../cicd/conf/feature/build.yaml
    
    commit 62d541ff8cc9fcca5c498e8f60cf4e01989428ca
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Feb 16 18:10:45 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Feb 16 18:10:45 2020 +0100
    
        [#4]: temporarily deactivate BashLib functions to mute output to stdout
    
    commit 4e1e95861385f1528d589670a600c4f15081ad76
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Feb 16 17:53:52 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Feb 16 17:53:52 2020 +0100
    
        [#4]: add script to return path to configuration templates root path
    
    commit c027e4816bafe57f0da99beabe07096e48d31129
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Feb 16 17:17:46 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Feb 16 17:17:46 2020 +0100
    
        [#4]: rename script from dd-dt-run-cont-images to dd-dt-run-image
    
    commit 62f3c4b6d810531556132227757bc094765c096e
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Feb 16 17:13:41 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Feb 16 17:13:41 2020 +0100
    
        [#4]: configure and run one single image only; script rename still due
    
    commit 1acc3c2496766a30b8ea20e6479cc793a9cfcc1d
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sat Feb 15 11:55:27 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sat Feb 15 11:55:27 2020 +0100
    
        [#4]: replace hardcoded values by template variables
    
    commit f4b13bbb2ab498199050b5a2c754ba2c7cb9f97a
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sat Feb 15 11:50:19 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sat Feb 15 11:50:19 2020 +0100
    
        [#4]: copy MailFlow Database > .../cicd/conf/feature/dev.yaml unchanged:
        
        serves as base for dd-dt-run-cont-images script configuration template
    
    commit 68f04ff38d527a7bbd276ab2235fa5c3cc7618a0
    Merge: 64c06e6 6a7b2b8
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sat Feb 15 10:12:20 2020 +0000
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sat Feb 15 10:12:20 2020 +0000
    
        Merge branch 'feature/3/use_in_production_and_improve' into 'develop'
        
        Feature/3/use in production and improve
        
        See merge request DesmoDyne/Tools/DockerTools!10
    
    commit 6a7b2b8e1686340d8e7ef961c24204dac393a832
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Mon Feb 10 12:54:59 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Mon Feb 10 12:56:45 2020 +0100
    
        [#3]: undo two most recent commits; unexpectedly break things
        
        this reverts commits
          515445be1730da62feca7078dc0f96df84d09fef
          eb11c358fea465c187967a7acb757a5e8279c575
    
    commit 515445be1730da62feca7078dc0f96df84d09fef
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Mon Feb 10 09:01:36 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Mon Feb 10 09:30:55 2020 +0100
    
        [#3]: align with backup script: pull backup/restore container
    
    commit eb11c358fea465c187967a7acb757a5e8279c575
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Feb 9 11:54:20 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Mon Feb 10 09:30:55 2020 +0100
    
        [#3]: begin to pull backup/restore container if not available locally:
        
        download / docker pull script needs its own conf file;
        halt development for now as this gets really messy real quick
    
    commit c2a3098637924ba81fb53ef6086178ef47616c59
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Feb 9 11:51:30 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Mon Feb 10 09:30:55 2020 +0100
    
        [#3]: don't exit, but continue upon error in loop; add TODO comment
    
    commit f26b9cf977f866b629ae00cd67f401661145f531
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Feb 9 06:55:30 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Mon Feb 10 09:30:55 2020 +0100
    
        [#3]: add TODO about exited containers that require manual removal
    
    commit aac014742fc53e1e3dd5234a00567d2558d02114
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Feb 9 06:38:04 2020 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Mon Feb 10 09:30:55 2020 +0100
    
        [#3]: support projects that do not configure images, but compositions
    
    commit ad72a0fb35a078f4ddd96f1ad23fcb05462e9bda
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Feb 4 21:24:41 2020 +1300
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Mon Feb 10 09:30:55 2020 +0100
    
        [#3]: do not specify python version 3 to use; make it default instead:
        
        this might have begun to fail after most recent brew update / upgrade
    
    commit 0239fd285993dea5553faa7b040be90a69b79f6f
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Jan 7 12:17:54 2020 +1300
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Jan 7 12:17:54 2020 +1300
    
        [#3]: do not take stage into account, but add to client vault path conf
    
    commit ab1f43a41a28601a49d3f79338ee9e08769c7713
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Fri Jan 3 12:46:43 2020 +1300
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Fri Jan 3 12:46:43 2020 +1300
    
        [#3]: update TODO comment about path_to_token_file / path_to_vault_token
    
    commit 3bf136e488fdc15b4c0f2a82a10cac4da6d85a9e
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Thu Dec 26 12:29:37 2019 +1300
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Thu Dec 26 12:29:37 2019 +1300
    
        [#3]: remove irrelevant fields for shorter, ideally one-line output
    
    commit 0edb69b74eb9e089ebe33c22a6b34867f216cc76
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Mon Dec 16 17:08:46 2019 +1300
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Mon Dec 16 17:08:46 2019 +1300
    
        [#3]: do not use pipenv for now; install req'd packages manually instead
    
    commit a896e4b4848ba08b0f028975a5b3c91df078dd1b
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Mon Dec 16 16:44:38 2019 +1300
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Mon Dec 16 16:44:38 2019 +1300
    
        [#3]: handle files to copy being configured per image or not;
        
        comment on unsatisfactory situation with fabric / pyyaml pip packages
    
    commit 283fd5d54473aabaa0a8d51d76da66c85b593c13
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Wed Dec 4 15:08:21 2019 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Wed Dec 4 15:08:21 2019 +0100
    
        [#3]: add files to copy from per-image conf
    
    commit e5789c535e4465c704ffd0ca44f12d3cade05e34
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Wed Dec 4 12:30:49 2019 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Wed Dec 4 12:30:49 2019 +0100
    
        [#3]: fix bug occurring when building multiple images subsequently
    
    commit cf0b9828233be937ae57ea16566793212ef091e3
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Tue Nov 5 15:10:01 2019 +0100
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Tue Nov 5 15:10:01 2019 +0100
    
        [#3]: do not list intermediate images
    
    commit 6bc538ca6e5369d9e68696edf4b56558584dc547
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Mon Oct 21 13:04:09 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Mon Oct 28 20:02:05 2019 +0100
    
        [#3]: deactivate full curl command in log output, exposes sensitive data
    
    commit 2204c4398b2501d31c433f07c4b72db2333009ee
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Mon Oct 21 13:01:32 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Mon Oct 28 20:02:05 2019 +0100
    
        [#3]: get stage from conf, use it to determine path into vault
    
    commit f9bb6a41d900d80d4fa84c69217459a3f5658f25
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Mon Oct 21 13:00:35 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Mon Oct 28 20:02:05 2019 +0100
    
        [#3]: display full curl command in log output for debugging
    
    commit 11e11132a39ddabebd7489d674c5abf54b2ce02c
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Wed Oct 16 11:54:44 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Mon Oct 28 20:02:05 2019 +0100
    
        [#3]: use a single container image tag: <stage>-<hash|semver>
    
    commit 9424591c86569f52328a4d8ebccfeb452b162f2b
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Wed Oct 2 13:42:44 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Wed Oct 2 13:42:44 2019 +0200
    
        [#3]: balance out creating/deleting folder; work around image tag issue
    
    commit d3576f6636efd3bbbfa159eeb70ee1bd01fa12e0
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Wed Oct 2 13:42:00 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Wed Oct 2 13:42:00 2019 +0200
    
        [#3]: pipenv install to make pip packs available in venv at first run
    
    commit c80230af37c36b706008de24defa4f3f082258a0
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Sep 29 20:02:57 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Sep 29 20:02:57 2019 +0200
    
        [#3]: fix bug introduced when aligning to latest BashLib functions
    
    commit 6d5908df2ab4d35f472c2c9c882985b4b74b4689
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sat Sep 28 11:30:23 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Sep 29 19:47:16 2019 +0200
    
        [#3]: yq use has been refactored out to BashLib, except for 1 occurrence
    
    commit 64c06e6997108df31f794eaeee0141ccc619b15e
    Merge: 772bdef 6c7cb4c
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sat Sep 28 11:04:13 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sat Sep 28 11:04:13 2019 +0200
    
        Merge tag '0.0.5' into develop
        
        automatically_created_release_tag 0.0.5
