#!/usr/bin/pyhton

import os


print ("😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵")

IP = input("IP:? ")

print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
os.system('echo rustscan -a '+IP)
rust_input = os.popen('rustscan -a '+IP).read()
c = rust_input.split()
rust = c[153::]

print (rust_input)

port_numbers = []

#Takes only the ports
a = [i for i,x in enumerate(rust) if x == "port"]
for port in a:
	port_numbers.append(rust[port+1])

#Takes only the numbers 
open_ports = []
for i in port_numbers:
    open_ports.append(i.split('/')[0])


#Remove "" and spaces
For_nmap = (','.join(open_ports))

print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#If you want to change the nmap options do it here
os.system ('echo nmap -sV -A -sC -p ' + (For_nmap) + " " +(IP))

os.system ('nmap -sV -A -sC -p ' + (For_nmap) + " " +(IP))

print ("The ip was: " + IP)

print (For_nmap)
ans = "no"
web_port=" "

for port in open_ports:
	if port == str(80) or port == str(8080) or port == str(8081) or port == str(443) or port == str(8000):
		print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		ans = input("Do you want to run gobuster?")
		web_port = port
		if ans == "yes" or ans == "y" or ans == "YES" or ans == "Y":
			print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
			##If you want to change the gobuster options do it here
			os.system('echo gobuster dir -w /usr/share/wordlists/dirb/common.txt -t 25 -x php,html,txt -q -u http://'+(IP)+":"+(web_port) )
			os.system('gobuster dir -w /usr/share/wordlists/dirb/common.txt -t 25 -x php,html,txt -q -u http://'+(IP)+":"+(web_port) )
		else: 
			print ("Ok good luck! and have a good day! IP: "+ (IP))	
	else:
		pass
