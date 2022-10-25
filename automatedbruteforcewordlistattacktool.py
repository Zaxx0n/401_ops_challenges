#!/usr/bin/env python3
# Script: Ops 401 Class 16 Automated Brute Force Wordlist Attack Tool Part 1 of 3

# Author: Zachary Derrick                    
# Date of latest revision:  10/24/22    
# Purpose: Begin to develop a custom tool that performs brute force attacks 
#          to better understand the types of automation employed by adversaries.

# Import Libraries
import time, getpass


def iterator():
    filepath = input("Please enter the filepath to your atck dictionary:\n")  or "/home/zaxxon/rockyou.txt"
    file = open(filepath)
    line = file.readline()
    print(line)
    #Loop
    while line: 
        line = line.rstrip()
        word = line
        print(word)
        time.sleep(.5)
        line = file.readline()
    file.close()    

def safepassword ():
    testpass = input("Enter word to search if it exists in atck dictionary:\n")
    filepath = input("Please enter the filepath to your atck dictionary:\n")  or "/home/zaxxon/rockyou.txt"
    with open(filepath, encoding ="latin1") as file:
        content = file.read()
        if testpass in content:
            print("That word is found in the atck dictionary.")
        else:
            print("Your word was not found in the atck dictionary.")
      
            
iterator()
safepassword()    