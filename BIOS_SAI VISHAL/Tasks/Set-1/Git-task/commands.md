Fork and then clone this repository to your local machine.
     COMMAND USED:
     git clone (url of the repositary)
     DESCRYPTION:
     it takes a copy of the repositary and displays it on the screen
Add a text file to this repository with your name as the file name the content should be the date that you attempted this task and commit it.
    COMMANDS USED:
    touch VISHAL
    DESCRYPTION:
    creates a new file
    cat > VISHAL
    DESCRYPTION:
    to write into the file
    git add VISHAL
    DESCRYPTION:
    now github tracks the file
    git commit -m "Date of completing task"
    DESCRYPTION:
    now it shows modified file and it is stored in local repositary.
Create a new branch with the your name as the branch name.
    COMMANDS USED:
    git checkout -b SAI_VISHAL
    DESCRYPTION:
    creates a new branch named SAI_VISHAL.
Add a markdown file to this new branch with your name as the file name and the content should be a brief description of yourself.
    COMMANDS USED:
    touch SAIVISHAL.md
    DESCRYPTION:
    creates a new file
    cat > SAIVISHAL.md
    DESCRYPTION:
    to write into the file
    git add SAIVISHAL.md
    DESCRYPTION:
    now it is tracked file
    git commit -m "Brief descryption of myself"
    DESCRYPTION:
    it accepts changes and stored it into local repositary
Now on the same markdown file add the commit hash of the last commit that you made when adding the text file then commit it.
    COMMANDS USED:
    git log
    DESCRYPTION:
    shows logs of previous commits.logs are to identify every commit we use.
    git add SAIVISHAL.md
    DESCRYPTION:
    it is tracked now.
    git commit -m "Brief descryption of myself,hash of last commit"
    DESCRYPTION:
    now it accepts changes and save it into local repositary
Merge the newly created branch with the main branch.
    COMMANDS USED:
    git checkout main
    DESCRYPTION:
    Now it is shifted to "main" branch
    git merge SAI_VISHAL
    DESCRYPTION:
    now SAI_VISHAL and main branches are merged.
Edit this README.md file to add your name at the very end of this file commit it then undo that very action using git reset.
    COMMANDS USED:
    git add README.md
    DESCRYPTION:
    it is a tracked file now.
    git commit -m "added my name into README.md file"
    DESCRYPTION:
    changes are accpeted and saved in local repositary.
    git log
    DESCRYPTION:
    shows hash of previous useed commits.
    git log
    git reset (url of previous commit)
    git log
    DESCRYPTION:
    use hash of previous commit in git reset command.
    Then after again typing git log it shows one less commit 
    git reset --hard (url of 1st commit)
    DESCRYPTION:
    There are 3 trees in github.
    1.THE HEAD
    2.THE INDEX
    3.Working Tree
    By using
    hard with reset the file is changed in all the trees.
    cat README.md
    DESCRYPTION:
    shows content in the README.md file
    now,my name is not in README.md file.
