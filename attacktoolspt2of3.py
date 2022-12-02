#!/usr/bin/env python3
# Script: Ops 401 Class 42 Attack Tools Part 2 of 3
# Author: Zachary Derrick                    
# Date of latest revision:  12/01/22    
# Purpose: use Python to develop a custom Nmap scanner that can later be combined 
#           with other Python scripts to create a pentester toolkit.

# This code can be found @ https://www.pythonpool.com/python-nmap/

import nmap

scanner = nmap.PortScanner()

print("Nmap Automation Tool")
print("--------------------")

ip_addr = input("IP address to scan: ") or "10.0.0.181"
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) OS Detection      
                \n""") 
print("You have selected option: ", resp)


if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    port_range = input("Please enter a port range to scan: ")
    scanner.scan(ip_addr, port_range, '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    # v is used for verbose, giving extra information
    # -sU means perform a UDP SYN connect scan, it sends the SYN packets to the host
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    # state() tells the user if target is up or down
    print("Ip Status: ", scanner[ip_addr].state())
    # all_protocols() tells which protocols are enabled like TCP UDP etc
    print("protocols:",scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    print(scanner.scan(ip_addr, arguments="-O")['scan'][ip_addr]['osmatch'][1])
    
else:
     print("Choose one of the three types of scans to perform: ") 
