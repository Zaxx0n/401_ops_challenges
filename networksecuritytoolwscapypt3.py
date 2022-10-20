#!/usr/bin/env python3
# Script: Ops 401 Class 11 Network Security Tools Part 3 of 3
# Author: Zachary Derrick                    
# Date of latest revision:  10/19/22    
# Purpose:  The final instalment of "Network Security Tools". The Super Scanner!
# Important Note:  This script was found and modeled after Mat Wood's script 
#                  found at https://thepacketgeek.com/scapy/building-network-tools/part-10/
#                  String to int conversion found at https://www.geeksforgeeks.org/python-get-a-list-as-input-from-user/ code example #5
import random
from ipaddress import IPv4Network
from typing import List
from scapy.all import ICMP, IP, sr1, TCP


# Define IP range to scan
network = input("Enter Network For Subnet Scan Plus* to Investiage \n(Includes Port Scanner)\n") or "10.0.0.0/30"
# Define TCP port range 
port_range = [int(item) for item in input("Enter the ports you'd like to check (separated by a comma) : ").split(",")]
# make list of addresses out of network, set live host counter
addresses = IPv4Network(network)
live_count = 0

def SuperScanner(host: str, ports: List[int]):
    # Send SYN with random Src Port for each Dst port
    for dst_port in ports:
        src_port = random.randint(1025, 65534)
        resp = sr1(
            IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,
            verbose=0,
        )
        if resp is None:
            print(f"IP: {host}:{dst_port} is filtered (silently dropped).")

        elif(resp.haslayer(TCP)):
            if(resp.getlayer(TCP).flags == 0x12):
                send_rst = sr1(
                    IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags='R'),
                    timeout=1,
                    verbose=0,
                )
                print(f"Hey, {host}:{dst_port} is open.")

            elif (resp.getlayer(TCP).flags == 0x14):
                print(f"Oh my! {host}:{dst_port} is closed.")

        elif(resp.haslayer(ICMP)):
            if(
                int(resp.getlayer(ICMP).type) == 3 and
                int(resp.getlayer(ICMP).code) in (1, 2, 3, 9, 10, 13)
            ):
                print(f"{host}:{dst_port} is filtered (silently dropped).")

# Send ICMP ping request, wait for answer
for host in addresses:
    if (host in (addresses.network_address, addresses.broadcast_address)):
        # Skip network and broadcast addresses
        continue

    resp = sr1(IP(dst=str(host))/ICMP(), timeout=2, verbose=0)

    if resp is None:
        print(f"{host} is down or not responding.")
    elif (
        int(resp.getlayer(ICMP).type)==3 and
        int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]
    ):
        print(f"{host} is blocking ICMP.")
    else:
        SuperScanner(str(host), port_range)
        live_count += 1

print(f"{live_count}/{addresses.num_addresses} hosts are online.")

