#!/usr/bin/env python3
# Script: Ops 401 Class 44 Create a Port Scanner
# Author: Zachary Derrick                    
# Date of latest revision:  12/16/22    
# Purpose:  determine if a target port is open or closed, using strictly Python 3 commands. 
# To do so, we’ll be importing the socket module a low-level networking interface for Python.

import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = socket.setdefaulttimeout(10)
sockmod.settimeout(timeout)

hostip = input("Please enter the host IP: ") 
portnumberinput = input("Which port would you like to check? ") 
portnumber = int(portnumberinput)
def portScanner(portnumber):
    if sockmod.connect_ex((hostip, portnumber)): 
        print("Port closed")
    else:
        print("Port open")

portScanner(portnumber)