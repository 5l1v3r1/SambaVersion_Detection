
#!/usr/bin/python

import os
import re
ip = raw_input("Enter IP Address: ")
port = raw_input("Enter SMB Port Number: ")

os.system("tcpdump -s0 -A -i tap0 port 139 -c 20 >> smbversion.txt &")
os.system("echo exit | smbclient -L \\\\"+ip)
with open ('smbversion.txt','r') as file:
        version = file.read()
        #print version
        searchobj = re.search(r'(Samba [\d].[\d].[\d\w].)', version, re.I)
        if searchobj:
                ver = searchobj.group(1)
                print "Samba Version: "+searchobj.group(1)
                ver = ver[:-3]
                os.system("searchsploit "+ver)
        else:
                print "Version not found."


