COMMAND1:git stash
DESCRIPTION:Now,changes are saved in the current branch.
COMMAND2:git checkout main
DESCRIPTION:Now,we have shifted to main branch from previous branch.
COMMAND3:git pull
DESCRIPTION:updated my local repo with my remote repo to get latest changes.
COMMAND4:git log
DESCRIPTION:to inspect the history of repo
COMMAND5:git show --name-only <hash>
DESCRIPTION:gives file(branch_name.txt)
COMMAND6:git show <hash>: branch_name.txt
DESCRIPTION:To see the contents in the file
OUTPUT:0PCF0703WM
COMMAND7:git checkout 0PCF0703WM
DESCRIPTION:To switch to that branch
COMMAND8:unzip protected.zip
DESCRIPTION:To unzip the file called protected.zip,i found that there is a .7z file
COMMAND9:7za x protected.7z.
OUTPUT:i got a gzipped file from that.
COMMAND10:gzip -d misc.zip.xz.zst.bz2.gz 
DESCRIPTION:To decompress that
OUTPUT:then i got a bz.2 file
COMMAND11:bzip2 -d misc.zip.xz.zst.bz2.
DESCRIPTION: now,i have got .zst compressed file
COMMAND12:zstd --decompress misc.zip.xz.zst
OUTPUT:another .xz compressed file
COMMAND13:xz --decompress.misc.zip.xz
OUTPUT:another zip file
COMMAND14:unzip misc.zip
OUTPUT:now an archive file has been appeared.
COMMAND15:tar -xf misc.tar
COMMAND16:cd misc
DESCRIPTION:to change to directory named misc
COMMAND17:ls misc | grep '^[0-9]\{2\}.*[0-9]\{2\}',
DESCRIPTION:shows the file that is started from 2 numbers and ended with 2 numbers
COMMAND18:cd <filename>
DESCRIPTION:to go to the folder  i got as the result of step9
COMMAND19:cat * > allfiles.txt
DESCRIPTION: to put the content of all files into allfiles.txt
COMMAND20:sort allfiles.txt > sort.txt
DESCRIPTION:sorts the combined content
COMMAND21:uniq -d sort.txt > doops.txt
DESCRIPTION:only keeps doop content
COMMAND22:sed 's/8/B/g' doop.txt > changed doop.txt
DESCRIPTION:removes all B's and replaces themw ith 8,"s" stands for substitute.
COMMAND23:touch <filename from above output>
DESCRIPTION:creates a new file named from the output.
COMMAND24:echo"I am learning Git" > <filename>
DESCRIPTION:inserted the message into the file
COMMAND25:git add <filename>
DESCRIPTION:Staged the file
COMMAND26:git commit -m "Created a new file"
DESCRIPTION:commited the new file
COMMAND27:git log
DESCRIPTION:shows the previous commits
COMMAND28:git revert <hash>
DESCRIPTION:removes the previous commit and goes to the stage to the previous commit
COMMAND29:nano <file.txt>
DESCRIPTION:to change content inside to I am learning Git and Linux
COMMAND30:git add <file.txt>
DESCRIPTION:stages the <file>
COMMAND31:git commit -m "Updated file"
DESCRIPTION: commited the file again and kept the message as Updated file
COMMAND32:touch writeup.md
OUTPUT:creates a new file named writeup.md
