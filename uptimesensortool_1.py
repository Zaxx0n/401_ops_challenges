#!/usr/bin/env python3
# Script: Ops 401 Class 02 Uptime Sensor Tool Part 1 of 2
# Author: Zachary Derrick                    
# Date of latest revision:  10/4/22    
# Purpose: Write an uptime sensor tool that checks systems are responding. 

# import libraries

import time
import datetime
import os


# declares variables 
hostname = input("Enter an IP address to check: ")
timestamp = datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")

# result = []

# declare functions
def updog():
    # hostname = "8.8.8.8"
    status = os.system("ping -c 1 " + hostname)  
    if status == 0:
            print("host", hostname, "is up!", timestamp)
            # result.append(timestamp)
            # print(result)
            # print("host 8.8.8.8 is up")
    else: 
            print("Host", hostname, "is down.", timestamp)
               
# print(result)

while True:
    updog()
    time.sleep(2)
# end
