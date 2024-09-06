# **<u>LEVEL11</u>**

**COMMAND(1)**:ls

**OUTPUT(1)**:shows data.txt file

**COMMAND(2)**:cat data.txt

**OUTPUT(2)**:VGhlIHBhc3N3b3JkIGlzIGR0UjE3M2ZaS2IwUlJzREZTR3NnMlJXbnBOVmozcVJyCg==

**COMMAND(3)**:base64 -d data.txt

**OUTPUT(3)**:gives password

# **<u>LEVEL12</u>**

**COMMAND(1)**:ls

**OUTPUT(1)**:shows data.txt file

**COMMAND(2)**:cat data.txt

**OUTPUT(2)**:Gur cnffjbeq vf 7k16JArUVv5LxVuJfsSVdbbtaHGlw9D4

**COMMAND(3)**:echo 'Gur cnffjbeq vf 7k16JArUVv5LxVuJfsSVdbbtaHGlw9D4' | tr 'A-Za-z' 'N-ZA-Mn-za-m'

**OUTPUT(3)**:shows password

# **<u>LEVEL13</u>**

**COMMAND(1)**:ls

**OUTPUT(1)**:shows data.txt file

**COMMAND(2)**:mkdir /tmp/bios

**OUTPUT(2)**: a new directory created under /tmp directory

**COMMAND(3)**:cp data.txt /tmp/bios

**OUTPUT(3)**:copies data.txt file into the new directory

**COMMAND(4)**:cd /tmp/bios

**OUTPUT(4)**:shifted to the directory /tmp/bios

**COMMAND(5)**:ls

**OUTPUT(5)**:data.txt

**COMMAND(6)**:xxd -r data.txt > data

**OUTPUT(6)**:decompresses the hexdump file by option -r and normally creates a hexdump file

**COMMAND(7)**:ls

**OUTPUT(7)**:shows the files

**COMMAND(8)**:file data

**OUTPUT(8)**:tells the type of data

**COMMAND(9)**:mv data file.gz

**OUTPUT(9)**:renames the file into .gz format

**COMMAND(10)**:gzip -d file.gz

**OUTPUT(10)**:for decompressing

**COMMAND(11)**:file file

**OUTPUT(11)**:tells the type of the file

**COMMAND(12)**:mv file file.bz2

**OUTPUT(12)**:renames the file

**COMMAND(13)**:bzip2 -d file.bz

**OUTPUT(13)**:compresses the fileq

**COMMAND(14)**:ls

**COMMAND(15)**:mv file file.tar

**OUTPUT(15)**:renames the file

**COMMAND(16)**:tar xf file.tar

**OUTPUT(16)**:to extract a tar archive

**COMMAND(17)**:ls

**COMMAND(18)**:file data5.bin

**OUTPUT(18)**:tells the type of file

**COMMAND(19)**:rm file.tar

**OUTPUT(19)**:removes the file

**COMMAND(20)**:rm data.txt

**OUTPUT(20)**:removes the file

**COMMAND(21)**:mv data5.bin data.tar

**OUTPUT(21)**:renames the file

**COMMAND(22)**:tar xf data.tar

**OUTPUT(22)**:extract the tar archive file

**COMMAND(23)**:ls

**COMMAND(24)**:file datat6.bin

**OUTPUT(24)**:tells the type of file

**COMMAND(25)**:mv data6.bin data.bz2

**OUTPUT(25)**:renames the file

**COMMAND(26)**:bzip2 -d data.bz2

**COMMAND(27)**:mv data data.tar

**OUTPUT(27)**:renames the file

**COMMAND(28)**:tar xf data.tar

**COMMAND(29)**:file data8.bin

**OUTPUT(29)**:tells the type of the file

**COMMAND(30)**:mv data8.bin data.gz

**OUTPUT(30)**:renames the file

**COMMAND(31)**:gzip -d data.gz

**COMMAND(32)**:file data

**OUTPUT(32)**:tells the type of data file

**COMMAND(33)**:cat data

**OUTPUT(33)**:shows password

# **<u>LEVEL14</u>**

**COMMAND(1)**:ls

**OUTPUT(1)**:sshkey.private

**COMMAND(2)**:ssh -p 2220 -l bandit14 -i sshkey.private bandit.labs.overthewire.org

**OUTPUT(2)**:goes to bandit level14

# **<u>LEVEL15</u>**

**COMMAND(1)**:cat /etc/bandit_pass/bandit14

**OUTPUT(1)**:gives the password that is to be submitted to the localhost

**COMMAND(2)**:nc localhost 30000

**OUTPUT(2)**:submit the above password to the localhost 30000 port and it will give us the new password.

# **<u>LEVEL16</u>**

**COMMAND(1)**:cat /etc/bandit_pass/bandit15

**OUTPUT(1)**:gives the password the previous level's password

**COMMAND(2)**:ncat --ssl localhost 30001

**OUTPUT(2)**:gives the final password

# **<u>LEVEL17</u>**

**COMMAND(1)**:cat /etc/bandit_pass/bandit16

**OUTPUT(1)**:gives the password that is to be submitted in local host

**COMMAND(2)**:nmap localhost -p 31000-32000

**OUTPUT(2)**:gives the port numbers which have server in them,

PORT      STATE SERVICE
31046/tcp open  unknown
31518/tcp open  unknown
31691/tcp open  unknown
31790/tcp open  unknown
31960/tcp open  unknown

**COMMAND(3)**:ncat --ssl localhost 31406

**OUTPUT(3)**:just checking if this the right port.but it is not :(

**COMMAND(4)**:ncat --ssl localhost 31518

**OUTPUT(4)**:just checking if this the right port.but it is not :(

**COMMAND(5)**:ncat --ssl localhost 31691

**OUTPUT(5)**:just checking if this the right port.but it is not :(

**COMMAND(6)**:ncat --ssl localhost 31790

**OUTPUT(6)**:gives the key to the next to level
