Output

Enter IP Address: 10.11.1.2
Enter SMB Port Number: 139
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on tap0, link-type EN10MB (Ethernet), capture size 262144 bytes
Server does not support EXTENDED_SECURITY  but 'client use spnego = yes' and 'client ntlmv2 auth = yes' is set
Anonymous login successful
Enter WORKGROUP\root's password: 

	Sharename       Type      Comment
	---------       ----      -------
	IPC$            IPC       IPC Service (Samba Server)
	ADMIN$          IPC       IPC Service (Samba Server)
Reconnecting with SMB1 for workgroup listing.
20 packets captured
30 packets received by filter
0 packets dropped by kernel
Server does not support EXTENDED_SECURITY  but 'client use spnego = yes' and 'client ntlmv2 auth = yes' is set
Anonymous login successful

	Server               Comment
	---------            -------
	BAY                  Samba Server
	TOT                  Samba Server

	Workgroup            Master
	---------            -------
	AE                   ORLE
	MROUP                BAY
	TC                   RPH
	TAL                  SUE
	WORKGROUP            B2
Samba Version: Samba 2.2.3a
------------------------------------------------------------------------------------------------------------- ----------------------------------------
 Exploit Title                                                                                               |  Path
                                                                                                             | (/usr/share/exploitdb/)
------------------------------------------------------------------------------------------------------------- ----------------------------------------
Samba 2.0.x/2.2 - Arbitrary File Creation                                                                    | exploits/unix/remote/20968.txt
Samba 2.2.0 < 2.2.8 (OSX) - trans2open Overflow (Metasploit)                                                 | exploits/osx/remote/9924.rb
Samba 2.2.2 < 2.2.6 - 'nttrans' Remote Buffer Overflow (Metasploit) (1)                                      | exploits/linux/remote/16321.rb
Samba 2.2.8 (BSD x86) - 'trans2open' Remote Overflow (Metasploit)                                            | exploits/bsd_x86/remote/16880.rb
Samba 2.2.8 (Linux Kernel 2.6 / Debian / Mandrake) - Share Privilege Escalation                              | exploits/linux/local/23674.txt
Samba 2.2.8 (Linux x86) - 'trans2open' Remote Overflow (Metasploit)                                          | exploits/linux_x86/remote/16861.rb
Samba 2.2.8 (OSX/PPC) - 'trans2open' Remote Overflow (Metasploit)                                            | exploits/osx_ppc/remote/16876.rb
Samba 2.2.8 (Solaris SPARC) - 'trans2open' Remote Overflow (Metasploit)                                      | exploits/solaris_sparc/remote/16330.rb
Samba 2.2.8 - Brute Force Method Remote Command Execution                                                    | exploits/linux/remote/55.c
Samba 2.2.x - 'call_trans2open' Remote Buffer Overflow (1)                                                   | exploits/unix/remote/22468.c
Samba 2.2.x - 'call_trans2open' Remote Buffer Overflow (2)                                                   | exploits/unix/remote/22469.c
Samba 2.2.x - 'call_trans2open' Remote Buffer Overflow (3)                                                   | exploits/unix/remote/22470.c
Samba 2.2.x - 'call_trans2open' Remote Buffer Overflow (4)                                                   | exploits/unix/remote/22471.txt
Samba 2.2.x - 'nttrans' Remote Overflow (Metasploit)                                                         | exploits/linux/remote/9936.rb
Samba 2.2.x - CIFS/9000 Server A.01.x Packet Assembling Buffer Overflow                                      | exploits/unix/remote/22356.c
Samba 2.2.x - Remote Buffer Overflow                                                                         | exploits/linux/remote/7.pl
Samba < 2.2.8 (Linux/BSD) - Remote Code Execution                                                            | exploits/multiple/remote/10.c
------------------------------------------------------------------------------------------------------------- ----------------------------------------
Shellcodes: No Result
