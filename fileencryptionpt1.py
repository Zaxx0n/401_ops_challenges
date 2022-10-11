#!/usr/bin/env python3
# Script: Ops 401 Class 06 File Encryption Script Part 1 of 3
# Author: Zachary Derrick                    
# Date of latest revision:  10/10/22    
# Purpose: Begin development of a Python script that encrypts a single file.

# import libraries
from cryptography.fernet import Fernet

# declare functions here

# function to declare key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()
# # function to load key
def load_key():
    return open("key.key", "rb").read()
load_key()
# load the generated key
key = load_key()

# input a message to encrypt
message = "Secret Message".encode()
# initialize the Fernet class
f = Fernet(key)

# encrypt and decrypt the message
encrypted = f.encrypt(message)

decrypted_encrypted = f.decrypt(encrypted)

# function to encrypt a file
def encrypt(test.txt, key):
    f = Fernet(key)
    with open(test.txt, "rb") as file:
        file_data = file.read

# main menu function
# def main_menu():
#     choice ='0'
#     while choice =='0':
#         print("Select a mode:")
#         print("Choose 1 to Encrypt a file")
#         print("Choose 2 to Decrypt a file")
#         print("Choose 3 to Encrypt a message")
#         print("Choose 4 to Decrypt a message")
#         print("Choose 5 to quit program")
#         choice = input("Please make a choice: ")

#     if choice == "5":
#         exit 
#     elif choice == "4":
#         print("Do Something 4")
#     elif choice == "3":
#         print("Do Something 3")
#     elif choice == "2":
#         print("Do Something 2")
#     elif choice == "1":
#         print("Do Something 1")
#     else:
#         print("That is not an option.")

# main_menu()
# load_key()

# if key == 0:
#     write_key()
# else:
#     main_menu()


print(encrypted)
print(decrypted_encrypted)

