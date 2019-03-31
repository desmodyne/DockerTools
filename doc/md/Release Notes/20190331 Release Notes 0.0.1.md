    commit 6b5caa08e60da4ceaa42bd2fe073a825b4edf4d3
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Mar 31 08:59:04 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Mar 31 08:59:04 2019 +0200
    
        [#1]: update project version
    
    commit cd12caf93fb78b6dd89f0b41f0c83b55f45a28c3
    Merge: ee2d4e7 6fea282
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Mar 31 06:54:37 2019 +0000
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Mar 31 06:54:37 2019 +0000
    
        Merge branch 'feature/2/refactor_docker_scripts_to_own_project' into 'develop'
        
        Feature/2/refactor docker scripts to own project
        
        See merge request DesmoDyne/Tools/DockerTools!1
    
    commit 6fea282bf847171f319ea3718b43f2e8d01effa2
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Mar 31 08:50:50 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Mar 31 08:50:50 2019 +0200
    
        [#2]: add license and minimal ReleaseTools project configuration file
    
    commit 11176d5abadf641e11de2f462d15c569375aee7a
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Mar 31 08:32:10 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Mar 31 08:32:10 2019 +0200
    
        [#2]: prepend dd- to script names to align with corporate conventions;
        
        done with
        
        $ cd "${HOME}/DevBase/DesmoDyne/Tools/DockerTools/code/bin"
        $ for old_name in *
          do
            new_name="dd-${old_name}"
            echo "old name: ${old_name}"
            echo "new name: ${new_name}"
            sed -e "s|${old_name}|${new_name}|g" "${old_name}" > "${new_name}"
            rm "${old_name}"
            echo
            echo
            echo
          done
        $ cd - > /dev/null
    
    commit 4a9885c3de993ad1fd963dc2e91d58e6251a097a
    Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    AuthorDate: Sun Mar 31 08:02:05 2019 +0200
    Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
    CommitDate: Sun Mar 31 08:02:05 2019 +0200
    
        [#2]: copy attic/cicd/bin and code folders from DesmoDyne source repo:
        
        at https://gitlab.com/DesmoDyne/Infrastructure/Services/tree/develop
        current commit: f9a9d5b13a0e8ec06f24c150bf441312ec0d9af9
    
