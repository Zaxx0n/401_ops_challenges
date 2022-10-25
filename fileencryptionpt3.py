#!/usr/bin/env python3
# Script: Ops 401 Class 06 File Encryption Script Part 3 of 3
# Author: Zachary Derrick                    
# Date of latest revision:  10/20/22    
# Purpose: A Script that is used to encrypt and decrypt data

# import libraries
from cryptography.fernet import Fernet
import os.path
import os
import sys 
import ctypes

# declare variables here
MB_HELP = 0x4000
MB_ICONHAND = 0x10

# function to declare key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# # function to load key
def load_key():
    return open("key.key", "rb").read()


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

# encrypt and decrypt the message
def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_bytes = f.encrypt(message.encode())
    return encrypted_bytes.decode('utf-8')
    

def decrypt_message(message, key):
    f = Fernet(key)
    decrypted_bytes = f.decrypt(message.encode())
    return decrypted_bytes.decode('utf-8')

# function to encrypt a directory 
def encrypt_dir(dir_path, key):
    for root, dirs, files in os.walk(dir_path):
        print('Directory: {:s}'.format(root))
        for file in files:
            filename = (os.path.join(root, file))
            encrypt_file(filename, key)

# function to decrypt a directory 
def decrypt_dir(dir_path, key):
    for root, dirs, files in os.walk(dir_path):
        print('Directory: {:s}'.format(root))
        for file in files:
            filename = (os.path.join(root, file))
            decrypt_file(filename, key)

# function for the ransom message
def ransome_ware():
    MessageBox = ctypes.windll.user32.MessageBoxW  # MessageBoxA in Python2
    MessageBox(None, 'ALL\nYOUR\nBASE\nARE\nBELONG\nTO\nUS', 'PAY US!', MB_HELP | MB_ICONHAND)

# main menu function
def main_menu():
    choice ='0'
    key=load_key()
    print("\n::::::::Secret Services::::::::")
    print("Choose 1 to Encrypt a File")
    print("Choose 2 to Decrypt a File")
    print("Choose 3 to Encrypt a Message")
    print("Choose 4 to Decrypt a Message")
    print("Choose 5 to Encrypt a Folder")
    print("Choose 6 to Decrypt a Folder")
    print("Choose 7 to Deploy Ransome Ware")
    print("Choose 8 to Quit Program")
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
        output = decrypt_message(message, key)
        print("\nDecrypted message is: " + output)
    elif choice == "5":
        dir_path = input("\nEnter the directory to be encrypted: ")
        encrypt_dir(dir_path, key)
    elif choice == "6":
        dir_path = input("Path to be Decrypted: ")
        decrypt_dir(dir_path, key)
    elif choice == "7":
        ransome_ware()
    elif choice == "8":
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



