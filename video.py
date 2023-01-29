import os
os.system("clear")
print("\033[;35;m___________________________________\n \n ")
print("\033[;35;mAmino :	\033[;33;mهــلوســه\n ")
print("\033[;35;minsta :	\033[;33;m5r5_9\n \n")
print("\033[;35;m___________________________________\n ")
import os,time
from multiprocessing import Process
from os import path
import hmac
from aminofix import exceptions
from hmac import new
from hashlib import sha1
import time
try:
	import json
	import aminofix	
	import requests
	import pyfiglet
except:
	os.system("pip install json-minify")
	os.system("pip install requests")
	os.system("pip install requests")
	os.system("pip install pyfiglet")
	import aminofix
	import requests
	import pyfiglet
	
os.system("clear")
A = "\033[1;91m"  #احمر
Z1 = '\033[2;31m' #احمر ثاني
E = "\033[1;92m"  #اخضر
H = "\033[1;93m" #اصفر
L = "\033[1;95m" #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح 
M = "\033[1;94m" #ازرك
t = "_"
p = H+"¥"
n = H+"1"+A
o = H+"2"+A
print(B+pyfiglet.figlet_format("    Join Video"))
print (L+"_ "*30)

def device_generator():
 identifier = os.urandom(20)
 return ("52" + identifier.hex() + new(bytes.fromhex("ae49550458d8e7c51d566916b04888bfb8b3ca7d"), b"\x52" + identifier, sha1).hexdigest()).upper()

prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
proxs= {'http': 'socks5://'+prox}
clint=aminofix.Client(device_generator() , proxies = proxs)
x=open("email.txt").read()
p = x.split('\n')
start=str(p).count(',')+1
o=clint.get_from_code(input('\033[;36;mchat Link : '))
j=o.objectId
o=o.path[1:o.path.index('/')]
password=input('\033[;36;mpassword  : ')
xb=0
for i in range(start):
	try:
		clint.login(email=p[i],password=password)
		print(f"\033[;32;mlogged in{email}")
		clint.join_community(comId=o)
		client.activity_status("on")
		subclint=aminofix.SubClient(comId=o,profile=clint.profile)
		subclint.join_chat(chatId=j)
		clint.join_video_chat_as_viewer(comId=o,chatId=j)
		xb+=1
	except:
		print (f"\n {p[i]}  ✅" ,i)