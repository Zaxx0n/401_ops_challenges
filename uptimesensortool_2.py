#!/usr/bin/env python3
# Script: Ops 401 Class 02 Uptime Sensor Tool Part 1 of 2
# Author: Zachary Derrick                    
# Date of latest revision:  10/4/22    
# Purpose: Write an uptime sensor tool that checks systems are responding. 
# import libraries

import time
import datetime
import os
import smtplib
import ssl
from email.message import EmailMessage

# declares variables
email_sender = "recyclops1970@gmail.com" # email information
email_password = input("Enter your password:") # email information
email_receiver = input("Please enter a valid email to recieve status results:") # email information

hostname = input("Enter an IP address to monitor: ")
timestamp = datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
last_ping = None
ping_status = None


# email subject & body
# subject = 'Host Status Updated'
# body = "host", hostname, "is up!", timestamp

# email message
# em = EmailMessage()
# em['From'] = email_sender
# em['To'] = email_receiver
# em['Subject'] = subject
# em.set_content(body)
# context = ssl.create_default_context()


# declare functions
def ping(targetIP):
    ping_status = os.system("ping -c 1 " + targetIP)
    if ping_status == 0:
        return True
    else :
        return False  

def getlastping():
    if ping_status == True:
        last_ping = "up"
    else : last_ping = "down"

def statuscheck():
    if ping_status != True & last_ping == False:
        sendmail()
    if ping_status == False & last_ping == True:
        sendmail()
     

# sending the emails
def sendmail():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver)
               
# main

while True:
    ping_status = ping(hostname)
    last_ping = getlastping()
    statuscheck()
    time.sleep(2)
# end
