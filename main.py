#!/usr/bin/python3
#pip install python-nmap

from concurrent.futures import thread
import time
from cgi import print_environ
from tokenize import Pointfloat
import nmap
from pystyle import Colorate, Colors, Write
import os
import socket 

def main():
    os.system('clear')
    print("""
======================================
__________             __          
\____    /____   _____/  |_ ___.__.
  /     // __ \ /    \   __<   |  |
 /     /\  ___/|   |  \  |  \___  |
/_______ \___  >___|  /__|  / ____|
        \/   \/     \/      \/    
======================================        
""")
    print("""
======================================================================================
$$\      $$\           $$\                 $$\      $$\                                         
$$$\    $$$ |          \__|                $$$\    $$$ |                                        
$$$$\  $$$$ | $$$$$$\  $$\ $$$$$$$\        $$$$\  $$$$ | $$$$$$\  $$$$$$$\  $$\   $$\   
$$\$$\$$ $$ | \____$$\ $$ |$$  __$$\       $$\$$\$$ $$ |$$  __$$\ $$  __$$\ $$ |  $$ | 
$$ \$$$  $$ | $$$$$$$ |$$ |$$ |  $$ |      $$ \$$$  $$ |$$$$$$$$ |$$ |  $$ |$$ |  $$ |
$$ |\$  /$$ |$$  __$$ |$$ |$$ |  $$ |      $$ |\$  /$$ |$$   ____|$$ |  $$ |$$ |  $$ |
$$ | \_/ $$ |\$$$$$$$ |$$ |$$ |  $$ |      $$ | \_/ $$ |\$$$$$$$\ $$ |  $$ |\$$$$$$  | 
\__|     \__| \_______|\__|\__|  \__|      \__|     \__| \_______|\__|  \__| \______/  
======================================================================================                                                                                                
                                                                                                
""")
    n = Write.Input("1- NetWork Scanner\n2- Vulnérabilities Detection\n3- Exploit\n\nPlease enter a number : ", Colors.blue_to_green, interval=0.0001)
    if n == '1':
        os.system('clear')
        networkscan()
    if n == '2':
        os.system('clear')
        vuln()
    if n == '3':
        os.system('clear')
        explmenu()
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
    os.system('clear')
    b = Write.Input("1- Vuln DOS\n2- Directory traversal\n3- SQL injection\n\nPlease enter a number : ", Colors.blue_to_green, interval=0.0001)
    if b == '1':
        os.system('clear')
        os.system('nmap -v --script dos ' + ip)
    if b == '2':
        os.system('clear')
        os.system('nmap -sV --script http-passwd ' + ip)
    if b == '3':
        os.system('clear')
        os.system('nmap -sV --script http-sql-injection ' + ip)
    else :
        print('Please choose a number between 1 ans 3')
    main()

def msf():
    print('This tool will start msfconsole and use a module so after this set all require things with $ show option ')
    time.sleep(5)
    os.system('/opt/metasploit-framework/bin/msfconsole ')
    os.system('use exploit/multi/http/atutor_sqli')

def attackddos():
    print("installing the script ...")
    time.sleep(2)
    os.system("pip install LITEDDOS")
    url = input("\nPlease enter the target URL address : ")
    port = input("\nPlease enter the target PORT : ")
    thr = input("\nPlease enter the number of THREAD of you want to use : ")
    print("So now type this ine a new terminal : python2 LITEDDOS.py " + url  + port + thr)

def explmenu():
    print("**********Welcome to the Exploit Menu**********")
    print("***********************************************")
    ip = input("\nPlease enter the target IP ")
    os.system('clear')
    b = Write.Input("1- DDOS Attack\n2- Directory Traversal\n3- SQL Injection\n\nPlease enter a number : ", Colors.blue_to_green, interval=0.0001)
    if b == '1':
        os.system('clear')
        attackddos()
    if b == '2':
        os.system('clear')
        os.system('nmap -sV --script http-passwd ' + ip)
    if b == '3':
        os.system('clear')
        os.system('nmap -sV --script http-sql-injection ' + ip)
    else :
        print('Please choose a number between 1 ans 3')
    main()




if __name__ == "__main__":
    main()

