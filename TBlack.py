#!/usr/bin/python3
import os
import time
from colorama import Fore, init
init()
print(Fore.CYAN)

banner = """
████████╗██████╗ ██╗      █████╗  ██████╗██╗  ██╗
╚══██╔══╝██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝
   ██║   ██████╔╝██║     ███████║██║     █████╔╝ 
   ██║   ██╔══██╗██║     ██╔══██║██║     ██╔═██╗ 
   ██║   ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗
   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝"""
print(banner)
print("created by Blacksterhack")

Disclaimer = """
This program was created for purposes only
"""
print(Disclaimer)

print(Fore.GREEN)


menu_scr = """
┌─┐─┐ ┬┌─┐┬  ┌─┐┌┬┐┌─┐┌┬┐┬┌─┐┌┐┌
├┤ ┌┴┬┘├─┘│  │ │ │ ├─┤ │ ││ ││││ 
└─┘┴ └─┴  ┴─┘└─┘ ┴ ┴ ┴ ┴ ┴└─┘┘└┘
1 - Metasploit
2 - Fsociety
┌─┐┬ ┬┬┌─┐┬ ┬┬┌┐┌┌─┐
├─┘├─┤│└─┐├─┤│││││ ┬
┴  ┴ ┴┴└─┘┴ ┴┴┘└┘└─┘
3 - NexPhisher
4 - HiddenEye
5 - BlackEye
6 - ZPhisher
7 - ShellPhish
8 - SocialPhish
9 - Seeker
10 - Evil SSDP
┌┐ ┬─┐┬ ┬┌┬┐┌─┐┌─┐┌─┐┬─┐┌─┐┌─┐
├┴┐├┬┘│ │ │ ├┤ ├┤ │ │├┬┘│  ├┤ 
└─┘┴└─└─┘ ┴ └─┘└  └─┘┴└─└─┘└─┘
11 - FBHT
12 - Hydra
13 - Jhon The Ripper
14 - SocialBox
15 - Instabrute
┬ ┬┌─┐┌┐ ┬ ┬┌─┐┌─┐┬┌─┬┌┐┌┌─┐
│││├┤ ├┴┐├─┤├─┤│  ├┴┐│││││ ┬
└┴┘└─┘└─┘┴ ┴┴ ┴└─┘┴ ┴┴┘└┘└─┘
16 - SrchX
17 - Awesome Web Hacking
18 - WhatWeb
19 - PHPSploit
20 - Jok3r

"""
print(menu_scr)

opt = int(input("Choose an option to install: "))

if opt==1:
	import subprocess
	subprocess.call('git clone https://github.com/rapid7/metasploit-framework', shell = True)
	os.system("clear")
	
	


if opt==2:
	import subprocess
	subprocess.call('git clone https://github.com/Manisso/fsociety', shell = True)
	os.system("clear")
	


if opt==3:
	import subprocess
	subprocess.call('git clone https://github.com/htr-tech/nexphisher', shell = True)
	os.system("clear")
	



if opt==4:
	import subprocess
	subprocess.call('git clone https://github.com/DarkSecDevelopers/HiddenEye-Legacy', shell = True)
	os.system("clear")
	

if opt==5:
	import subprocess
	subprocess.call('git clone https://github.com/An0nUD4Y/blackeye', shell = True)
	os.system("clear")
	

if opt==6:
	import subprocess
	subprocess.call('git clone https://github.com/htr-tech/zphisher', shell = True)
	os.system("clear")


if opt==7:
	import subprocess
	subprocess.call('git clone https://github.com/suljot/shellphish', shell = True)
	os.system("clear")


if opt==8:
	import subprocess
	subprocess.call('git clone https://github.com/UndeadSec/SocialFish', shell = True)
	os.system("clear")

if opt==9:
	import subprocess
	subprocess.call('git clone https://github.com/thewhiteh4t/seeker', shell = True)
	os.system("clear")

if opt==10:
	import subprocess
	subprocess.call('git clone https://github.com/initstring/evil-ssdp', shell = True)
	os.system("clear")


if opt==11:
	import subprocess
	subprocess.call('git clone https://github.com/chinoogawa/fbht', shell = True)
	os.system("clear")

if opt==12:
	import subprocess
	subprocess.call('git clone https://github.com/vanhauser-thc/thc-hydra', shell = True)
	os.system("clear")


if opt==13:
	import subprocess
	subprocess.call('git clone https://github.com/openwall/john', shell = True)
	os.system("clear")

if opt==14:
	import subprocess
	subprocess.call('git clone https://github.com/Cyb0r9/SocialBox', shell = True)
	os.system("clear")


if opt==15:
	import subprocess
	subprocess.call('git clone https://github.com/chinoogawa/instaBrute', shell = True)
	os.system("clear")

if opt==16:
	import subprocess
	subprocess.call('git clone https://github.com/Blacksterhack/SrchX', shell = True)

if opt==17:
	import subprocess
	subprocess.call('https://github.com/infoslack/awesome-web-hacking', shell = True)


if opt==18:
	import subprocess
	subprocess.call('https://github.com/urbanadventurer/WhatWeb', shell = True)


if opt==19:
	import subprocess
	subprocess.call('https://github.com/nil0x42/phpsploit', shell = True)

if opt==20:
	import subprocess
	subprocess.call('https://github.com/koutto/jok3r', shell = True)