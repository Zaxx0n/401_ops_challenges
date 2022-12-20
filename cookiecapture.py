#!/usr/bin/env python3
# Script: Ops 401 Class 37 Cookie Capture Capades
# Author: Zachary Derrick                    
# Date of latest revision:  12/20/22    
# Purpose: capture a cookie and send it back out to the site in order to receive a valid response in HTTP text
#          all using Python’s Requests module
# Resources: https://emojicombos.com/cookie-monster-ascii-art
#           https://stackoverflow.com/questions/50329050/save-load-html-response-as-object-in-a-file-python
# The below Python script shows one possible method to return the cookie from a site that supports cookies.

import requests, os

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Found a completed Cookie Monster searching for ASCII art.
    print('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣶⣿⣿⠿⠿⠛⠛⠛⠛⠛⠻⠿⢿⣿⣷⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⡿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠿⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡟⠉⠀⠀⠀⠀⠀⠀⢀⡤⠶⠶⢤⡀⡴⠛⠉⠀⠉⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⢟⠙⣟⣷⣴⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⢠⠏⠀⣶⣶⣦⠟⠃⠀⣠⣄⠀⠀⢹⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡷⣿⢀⡟⠛⠛⠯⣄⠀⠀⠀⠀⠀⠀⠀⠀⣺⡀⠀⠈⠛⠁⠀⣆⠀⢿⡿⠀⢀⠞⠉⠩⠽⢷⣤⣀⠀⠀⠀⠀⠀⠀⠘⢿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣷⣿⣸⣷⡀⠀⠀⡘⣷⡀⠀⠀⠀⣷⣶⠛⠉⠳⣄⣀⣀⣠⠞⠀⠙⠒⠶⠚⠉⠀⠀⠀⠀⠀⠀⢽⣷⡀⡀⠀⠀⠀⠀⠈⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⠏⠙⣷⣦⡀⠛⠻⡇⠀⣠⣿⠉⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣦⠐⢯⡽⠃⠀⠀⠀⠀⠀⠈⣿⣿⣤⣤⣀⠀⠀⠀⠀⠀
⠀⠀⣠⣾⡿⠋⢡⣤⢠⣤⣾⡏⠀⣄⠀⣿⠀⣿⠋⢠⠆⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣀⣀⣦⣤⣤⣬⣿⣿⡇⠉⠀⢀⢷⠀⠀⠀⠀⣠⢴⠛⠋⢡⡤⢨⣹⡇⠀⠀⠀⠀
⢀⣼⣻⠋⢀⡀⠈⠀⠘⣻⣿⣳⡤⠤⠴⣧⣸⡇⠀⠘⠛⢿⣯⣤⣴⣾⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣅⡀⠀⠘⡞⠀⠀⢀⣼⡣⠾⠃⠀⠈⢃⡼⣹⡇⠀⠀⠀⠀
⢸⣿⠃⠀⠿⠃⢀⠀⢠⣯⣴⠆⠀⠀⠰⠶⠀⢿⣧⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣶⠈⠙⢦⡟⢿⣄⢠⡿⠁⣰⡄⠀⡾⢁⣾⣴⠟⠀⠀⠀⠀⠀
⠸⣿⡀⢼⠀⢘⣿⡴⠟⠁⠀⠀⣶⠆⣀⡤⢀⣼⠏⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⢿⠏⠉⢙⡀⢠⡀⠠⢸⡀⠀⠋⢿⣅⠀⣽⠟⠓⡶⢯⣼⡏⠀⠀⠀⠀⠀⠀
⠀⠘⠻⠶⠶⣟⡛⠲⠤⠀⠒⢒⠋⣉⣵⠶⡞⠻⣤⠀⠀⣀⣤⢞⡟⢻⣷⠀⠉⠛⢿⣿⡔⣆⠻⠆⠘⠛⣾⠻⣦⣌⣧⠀⠀⠀⠙⣿⡧⡇⠀⠿⠏⠻⢷⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠙⣿⣟⠉⠉⠉⠙⠻⢧⣄⣹⡶⠾⠛⠉⠁⢀⡼⠁⠈⠁⠀⠀⣠⡄⠻⢿⣮⡀⣄⡀⠀⠹⣆⠀⠈⠙⠳⠶⢦⡀⠘⡇⣇⠸⢷⠀⠀⢀⡹⣧⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⢦⠀⣰⢾⠟⠉⠀⢀⣤⡴⠶⠿⠦⣤⣤⡴⢞⡇⠉⠁⢸⠘⡏⠙⠻⣮⣯⣄⣹⣧⣀⠀⠀⠀⠀⠙⣆⠹⣞⢆⠀⢠⣄⠈⠻⠻⡆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⣿⡆⠰⠀⣼⠋⠀⠀⠀⠈⠉⠀⣀⠀⠀⠀⠀⠀⢴⡞⣴⡄⠀⢸⢂⡇⣀⣤⣧⡙⠓⠦⠶⠚⠳⠦⣄⠀⠀⠈⢦⠹⣎⢦⡈⠉⠀⣀⢀⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⡄⢠⠇⠀⠀⠀⠀⠀⠀⣠⠟⠾⠤⠤⢤⣴⣋⡀⠀⢀⣠⠟⣾⡷⠛⠹⡟⡿⠄⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⢈⣿⣝⣦⣠⣤⣼⣇⣀⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣾⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠈⢉⣹⠿⣧⣴⣿⠁⠀⣀⣀⣙⣶⣄⣀⣀⣀⠀⠀⠀⠈⢀⣤⠶⠛⣩⣥⠀⠀⠀⠠⡦⠈⢻⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠒⠒⠶⢤⣤⣤⠟⠋⢹⠇⠙⢻⣧⠀⢾⣧⣉⠉⠉⠀⠀⠀⠈⠙⠦⠀⢠⡟⢱⣤⠀⠈⠁⠀⠻⠀⣀⡤⢀⣼⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣧⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠹⠦⢤⡾⠀⠀⣤⡛⣧⢤⡈⠙⣻⣒⣀⠀⠀⠀⠀⠀⠀⢿⣜⠲⠤⠄⠠⠔⠒⠒⢉⣡⡶⠟⠋⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣦⡀⠀⠀⣀⡀⠀⠀⠀⣀⡠⠶⣫⡤⠀⠀⠈⠀⢸⣧⡹⢄⣉⡋⢹⡟⠲⠦⠀⢀⣠⣾⣿⠋⠛⠛⠛⠛⠛⠋⠉⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣦⣄⣠⠿⠋⠉⠉⣏⠀⡀⠀⠀⠀⠶⠀⠀⣸⠀⠉⠳⠾⢭⣭⣇⠀⣀⣴⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣶⣤⣀⡀⠙⠷⣍⡓⠀⣆⣖⣢⡴⠋⠀⠀⠀⠀⣀⣠⣼⣾⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⣿⣶⣶⣭⣭⣭⣭⣤⣤⣤⣴⣶⣿⣿⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠛⠋⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

html = requests.get(targetsite, cookies=cookie)
content = html.text

# open with 'w' is to write overwriting any existing content 
with open ('cookiecookie.html', 'w') as f:
  f.write(content)

os.system("firefox /home/kali/Desktop/cookiecookie.html")
