#!/usr/bin/python3
#pip install python-nmap

import time
from cgi import print_environ
from tokenize import Pointfloat
import nmap
from pystyle import Colorate, Colors, Write
import os
import socket 

print("""__________             __          
\____    /____   _____/  |_ ___.__.
  /     // __ \ /    \   __<   |  |
 /     /\  ___/|   |  \  |  \___  |
/_______ \___  >___|  /__|  / ____|
        \/   \/     \/      \/    """)

def main():
    print("""
$$\      $$\           $$\                 $$\      $$\                                         
$$$\    $$$ |          \__|                $$$\    $$$ |                                        
$$$$\  $$$$ | $$$$$$\  $$\ $$$$$$$\        $$$$\  $$$$ | $$$$$$\  $$$$$$$\  $$\   $$\   
$$\$$\$$ $$ | \____$$\ $$ |$$  __$$\       $$\$$\$$ $$ |$$  __$$\ $$  __$$\ $$ |  $$ | 
$$ \$$$  $$ | $$$$$$$ |$$ |$$ |  $$ |      $$ \$$$  $$ |$$$$$$$$ |$$ |  $$ |$$ |  $$ |
$$ |\$  /$$ |$$  __$$ |$$ |$$ |  $$ |      $$ |\$  /$$ |$$   ____|$$ |  $$ |$$ |  $$ |
$$ | \_/ $$ |\$$$$$$$ |$$ |$$ |  $$ |      $$ | \_/ $$ |\$$$$$$$\ $$ |  $$ |\$$$$$$  | 
\__|     \__| \_______|\__|\__|  \__|      \__|     \__| \_______|\__|  \__| \______/  
                                                                                                
                                                                                                
                                                                                                
""")
    n = Write.Input("1- NetWork Scanner\n2- Vulnérabilities Detection\n3- Exploit\n\nPlease enter a number : ", Colors.blue_to_green, interval=0.0001)
    if n == '1':
        networkscan()
    if n == '2':
        vuln()
    if n == '3':
        expl()
    else :
        print('Please choose a nnumber between 1 ans 3')

def networkscan():
    print("**********Welcome to the Network Scanner**********")
    print("**************************************************")
    ip = input("Enter the target IP : ")
    os.system('nmap ' + ip)
    main()

def vuln():
    print("**********Welcome to the Vulnerabilities scanner**********")
    print("**********************************************************")
    ip = input("\nPlease enter the IP address : ")
    b = Write.Input("1- Vuln DOS\n2- Directory traversal\n3- SQL injection\n\nPlease enter a number : ", Colors.blue_to_green, interval=0.0001)
    if b == '1':
        os.system('nmap -v --script dos ' + ip)
    if b == '2':
        os.system('nmap -sV --script http-passwd ' + ip)
    if b == '3':
        os.system('nmap -sV --script http-sql-injection ' + ip)
    else :
        print('Please choose a number between 1 ans 3')
    main()

def expl():
    print('This tool will start msfconsole and use a module so after this set all require things with $ show option ')
    time.sleep(5)
    os.system('/opt/metasploit-framework/bin/msfconsole ')
    os.system('use exploit/multi/http/atutor_sqli')


if __name__ == "__main__":
    main()

