#!/usr/bin/env python3
# Script: Ops 401 Class 11 Network Security Tools Part 1 of 3
# Author: Zachary Derrick                    
# Date of latest revision:  10/17/22    
# Purpose:  Begin development of my own network scanning tool.

# import libraries 
import random
from sys import flags
from scapy.all import sr1, sr, IP, ICMP, TCP

host = "10.0.0.181"
# sport, scan port range...yeah, sport
sport = (20, 21, 22, 80)
src_port = 22
for port in sport:
    response=sr1(IP(dst=host)/TCP(sport=src_port,dport=port,flags="S"),timeout=1,verbose=0,) 
    if response is not None and response.haslayer(TCP):
        print(str(port)) +": "
    if response is not None and response.haslayer(TCP) and response.getlayer(TCP).flags==0x12:
        print("Hey," + str(sport) +": is open")
    if response is not None and response.haslayer(TCP) and response.getlayer(TCP).flags==0x14:
        print("Oh my," + str(sport) +": is closed")
    else:
        print(str(port) +" is filtered and silently dropped")

# p=sr1(IP(dst=host)/TCP(sport))
# if p:
#     p.show()


# def hostIP ():
#     input("Enter a Host IP: ")
#     host = hostIP()

# def portrange ():
#     input("Enter the port(s) to scan: ")
#     sport = portrange

# def main_menu():
#     choice ='0'
#     print("\n::::::::Scapy Services::::::::")
#     print("Choose 1 to Enter Host IP")
#     print("Choose 2 to Set Range of Ports")
# #     print("Choose 3 to Scan Port Range")
#     print("Choose 0 to Quit Program")
#     choice = input("Please make a choice: ")
#     if choice == "1":
#         hostIP()
#     elif choice == "2":
#         portrange()
#     elif choice == "0":
#         sys.exit("\nIf you want to keep a secret, you must also hide it from yourself.")
#     else:
#         print("\nThat is not an option.")
    
# # # main 

# while True:
#     main_menu()