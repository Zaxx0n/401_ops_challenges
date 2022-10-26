#!/usr/bin/env python3
# Script: Ops 401 Class 16 Automated Brute Force Wordlist Attack Tool Part 1 of 3

# Author: Zachary Derrick                    
# Date of latest revision:  10/25/22    
# Purpose: Continuation of a custom tool that performs brute force attacks 
#          to better understand the types of automation employed by adversaries.

# Import Libraries
import time, getpass, paramiko, sys, os, socket
from pexpect import pxssh

global host, username, line, input_file

def iterator():
    filepath = input("Please enter the filepath to your password dictionary:\n")  or "/home/zaxxon/rockyou.txt"
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

def dictpath():
    passdict = input("Please enter the filepath to your password dictionary:\n") or "/home/zaxxon/rockyou.txt"
    return passdict

def safepassword(pathtodict):
    testpass = input("Enter password to check against password dictionary:\n")
    with open(pathtodict, encoding="latin1") as file:
        content = file.read()
        if testpass in content:
            print("That word is found in the atck dictionary.\n")
            retry = input("Would you like to test another password?\n(Yes/No)\n")
            if retry.lower() == "yes" or retry.lower() == "y":
                safepassword(pathtodict)
            elif retry.lower() == "no" or retry.lower() == "n":
                sys.exit("Good, I was done with you anyways. ( ◣∀◢)ψ")
        else:
            print("Your word was not found in the atck dictionary.\n")
            continue_to_main_menu = input("Would you like to return to the main menu?")
            if continue_to_main_menu.lower() == "yes" or continue_to_main_menu.lower() == "y":
                main_menu()
            elif continue_to_main_menu.lower() == "no" or continue_to_main_menu.lower() == "n":
                sys.exit("Your password is safe with me. ( ◣∀◢)ψ")
            else: 
                print("Was that a yes or a no?")   
      
            
# iterator()
# safepassword()   

# sample of SSH authentication


# session = pxssh.pxssh()
# host = input("Please provde an IP address: ") or "10.0.0.81"
# username = input("Please provide a username: ") or "splunkadmin"
# passwrd = getpass.getpass(prompt = "Enter a password: ") or "splunkadmin"


# try:
#     session.login(host, username, passwrd)
#     session.sendline("uptime")
#     session.prompt()
#     print(session.before) #print everything before the prompt
#     session.sendline("whoami")
#     session.prompt()
#     print(session.before)
#     session.sendline("ls -l")
#     session.prompt()
#     print(session.before)
#     session.logout()

# except pxssh.ExceptionPxssh as e:
#     print("pxssh failed on login.")
#     print(e)

def main_menu():
    choice ='0'
    print("\n::::::::Pa$$w0rd ☠️H҉A҉C҉K҉E҉R҉☠️::::::::")
    print("Choose 1 to Check Password Strength Against Common Password List")
    # print("Choose 2 to Decrypt a File")
    # print("Choose 3 to Encrypt a Message")
    # print("Choose 4 to Decrypt a Message")
    # print("Choose 5 to Encrypt a Folder")
    # print("Choose 6 to Decrypt a Folder")
    print("Choose 0 to Quit Program")
    choice = input("Please make a choice: ")
    if choice == "1":
        safepassword(dictpath())   
    # elif choice == "2":
    #     file_path = input("\nEnter the file path of the file to decrypt: ")
    #     decrypt_file(file_path, key)
    # elif choice == "3":
    #     message = input("\nInput message to encrypt: ")
    #     output = encrypt_message(message, key)
    #     print("\nCiphertext is: " + output)
    # elif choice == "4":
    #     message = input("\nInput message to decrypt: ")
    #     output = decrypt_message(message, key)
    #     print("\nDecrypted message is: " + output)
    # elif choice == "5":
    #     dir_path = input("\nEnter the directory to be encrypted: ")
    #     encrypt_dir(dir_path, key)
    # elif choice == "6":
    #     dir_path = input("Path to be Decrypted: ")
    #     decrypt_dir(dir_path, key)
    elif choice == "0":
        sys.exit("\nIf you want to keep a secret, you must also hide it from yourself.")
    else:
        print("\nThat is not an option.")


while True:
    main_menu()
# 10.0.0.81/24