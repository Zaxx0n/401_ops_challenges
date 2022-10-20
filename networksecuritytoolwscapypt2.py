#!/usr/bin/env python3
# Script: Ops 401 Class 12 Network Security Tools Part 2 of 3
# Author: Zachary Derrick                    
# Date of latest revision:  10/18/22    
# Purpose:  Next step of development of my own network scanning tool.
# Important Note:  This script was found and modeled after Mat Wood's script at https://thepacketgeek.com/scapy/building-network-tools/part-10/

# import libraries 
import random
import sys
from scapy.all import sr1, sr, IP, ICMP, TCP
from ipaddress import IPv4Network

# host = ()
# IP to test 10.0.0.181, 10.0.0.80, 10.0.0.199, 10.0.0.133
def tcpscan():
    host = input("\nEnter IP to perform tcp scan on: ") or "10.0.0.80"
    port_range = (20, 22, 23, 80, 443, 3389, 8000)
    for dst_port in port_range:
        src_port = random.randint(1025, 65534)
        resp = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,verbose=0)
        if resp is None: 
            print(f"{host}:{dst_port} is filtered (silently dropped).")
        elif (resp.haslayer(TCP)):
            if(resp.getlayer(TCP).flags==0x12):
                print(f"Hey, {host}:{dst_port} is open")
            elif(resp.getlayer(TCP).flags==0x14):
                print(f"Oh my, {host}:{dst_port} is closed")
        
           
def ping_sweep():
    network = input("\nEnter IP in CIDR Notation: ")
    ipadd = IPv4Network(network)
    live_count = 0

    for host in ipadd:
        if (host in (ipadd.network_address, ipadd.broadcast_address)):
            continue

        resp = sr1(IP(dst=str(host))/ICMP(),timeout=2,verbose=0,)

        if resp is None:
            print(f"{host} is down or not responding")
        elif (
        int(resp.getlayer(ICMP).type)==3 and
        int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]
    ):
            print(f"{host} is blocking ICMP.")
        else:
            print(f"{host} is responding.")
            live_count += 1

    print(f"{live_count}/{ipadd.num_addresses} hosts are online.")    


def main_menu():
    choice ='0'
    print("\n::::::::Scapy Services::::::::")
    print("1 - TCP Scanner")
    print("2 - Ping Sweep")
    print("0 - Quit Program")
    choice = input("Please make a choice: ")
    if choice == "1":
        tcpscan()
    elif choice == "2":
        ping_sweep()
    elif choice == "0":
        sys.exit("\nIf you want to keep a secret, you must also hide it from yourself.")
    else:
        print("\nThat is not a valid option.")
    
# main 

while True:
    main_menu()