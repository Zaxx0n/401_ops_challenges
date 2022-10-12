#!/usr/bin/env python3
# Script: Ops 401 Class 06 File Encryption Script Part 1 of 3
# Author: Zachary Derrick                    
# Date of latest revision:  10/11/22    
# Purpose: Begin development of a Python script that encrypts a single file.

# import libraries
from cryptography.fernet import Fernet
import os.path
import sys 
# declare variables here

# function to declare key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# # function to load key
def load_key():
    return open("key.key", "rb").read()


# encrypt and decrypt the message
def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_bytes = f.encrypt(message.encode())
    return encrypted_bytes.decode('utf-8')
    

def decrypt_message(message, key):
    f = Fernet(key)
    decrypted_bytes = f.decrypt(message.encode())
    return decrypted_bytes.decode('utf-8')


# function to encrypt a file
def encrypt_file(file_path, key):
    f = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
        encrypted_data =f.encrypt(file_data)
        with open(file_path, "wb") as file:
            file.write(encrypted_data)

# function to decrypt a file 
def decrypt_file(file_path, key):
    f = Fernet(key)  
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data) 
        with open(file_path, "wb") as file:
            file.write(decrypted_data)    

# main menu function
def main_menu():
    choice ='0'
    key=load_key()
    print("\n::::::::Encryption Sevices::::::::")
    print("Choose 1 to Encrypt a file")
    print("Choose 2 to Decrypt a file")
    print("Choose 3 to Encrypt a message")
    print("Choose 4 to Decrypt a message")
    print("Choose 5 to quit program")
    choice = input("Please make a choice: ")
    if choice == "1":
        file_path = input("\nEnter the file path of the file to encrypt: ")
        encrypt_file(file_path, key)      
    elif choice == "2":
        file_path = input("\nEnter the file path of the file to decrypt: ")
        decrypt_file(file_path, key)
    elif choice == "3":
        message = input("\nInput message to encrypt: ")
        output = encrypt_message(message, key)
        print("\nCiphertext is: " + output)
    elif choice == "4":
        message = input("\nInput message to decrypt: ")
        output = decrypt_message (message, key)
        print("\nDecrypted message is: " + output)
    elif choice == "5":
        sys.exit("\nIf you want to keep a secret, you must also hide it from yourself.")
    else:
        print("\nThat is not an option.")
    
# main 
if os.path.isfile("key.key") == False:
    write_key()
    load_key()

while True:
    main_menu()



# end



