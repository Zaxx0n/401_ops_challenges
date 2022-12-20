#!/usr/bin/env python3
# Script: Ops 401 Class 36 Web Application Fingerprinting Part 1 of 3
# Author: Zachary Derrick                    
# Date of latest revision:  12/20/22    
# Purpose: Begin develop a Python script that utilizes 
#           multiple banner grabbing approaches against a single target.
# Resources: https://www.instructables.com/Netcat-in-Python/#:~:text=Introduction%3A%20Netcat%20in%20Python&text=In%20essence%2C%20netcat%20allows%20you,Datagram%20Protocol%2C%20and%20is%20connectionless.

import nmap, socket, subprocess, os, time, sys
 

destination = input("Enter IP or URL to Scan: ") or "scanme.nmap.org"
portnumberinput = input("Which port would you like to check? ")
portnumber = int(portnumberinput)

def netcat(destination, portnumber):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((destination, portnumber))
    run = "Netcat " + destination + " " + portnumberinput
    sock.sendall(run.encode())
    sock.shutdown(socket.SHUT_WR)
    res = " "

    while True:
        data = sock.recv(1024)
        if (not data):
            break
        res += data.decode()

    print(res)

    sock.close()

def nmap(destination, portnumber):
    os.system("Nmap -Pn -p " + portnumberinput + " -sV -script=banner " + destination + " | grep banner")

# Declare telnet fingerprinting function
def telnet(destination, portnumber):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((destination, int(portnumber)))
    run = "telnet " + destination + " " + portnumberinput
    sock.sendall(run.encode())
    sock.shutdown(socket.SHUT_WR)

    res = " "

    while True:
        data = sock.recv(1024)
        if (not data):
            break
        res += data.decode()

    print(res)

    sock.close()

# Main
response = input("""\nPick a Banner Grabber: 
                1) Netcat
                2) Nmap
                3) Telnet\n""")
print("You have selected option: ", response)
 
# If user's input is 1, perform a banner grabbing using Netcat
if response == '1':
    print("Netcat Results: ")
    netcat(destination, portnumber)
   
     
# # If user's input is 2, perform a banner grabbing using Nmap
elif response == '2':
    print("Nmap Results: ")
    nmap(destination, portnumber)
    
     
# If user's input is 3, perform a banner grabbing using Telnet
elif response == '3':
    print("Telnet Results: ")
    telnet(destination, portnumber)
  
     
else:
    print("\nPlease choose a number from the options above")



