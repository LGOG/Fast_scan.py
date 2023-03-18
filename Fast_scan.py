#!/usr/bin/pyhton
#Importing
import os
import re

print ("😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵")

#User input for IP
IP = input("Which IP would you like me to scan? ")

print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#Fast rustscan
os.system('echo rustscan -a '+IP)
rust_input = os.popen('rustscan --ulimit 5000 -a '+IP).read()

#Takes only the ports
port_list = re.findall(r'\d+/tcp', rust_input)
port_list = [port.split('/')[0] for port in port_list]
port_list = list(dict.fromkeys(port_list))
ports = ','.join(port_list)

print (rust_input)

print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

#Nmap deep scan
#If you want to change the nmap options do it here
os.system ('echo nmap -T4 -A -sC -p ' + (ports) + " " +(IP))
os.system ('nmap -T4 -A -sC -p ' + (ports) + " " +(IP))
print ("The ip was: " + IP)
print (ports)

#Web scan
for port in port_list:
	if port == str(80) or port == str(8080) or port == str(8081) or port == str(443) or port == str(8000):
		print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		ans = input("Do you want to run gobuster?")
		web_port = port
		if ans == "yes" or ans == "y" or ans == "YES" or ans == "Y":
			print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
			##If you want to change the gobuster options do it here
			os.system('echo gobuster dir -w /usr/share/dirb/wordlists/common.txt -t 25 -x php,html,txt -q -u http://'+(IP)+":"+(web_port) )
			os.system('gobuster dir -w /usr/share/dirb/wordlists/common.txt -t 25 -x php,html,txt -q -u http://'+(IP)+":"+(web_port) )
		else: 
			pass	
	else:
		print ("Ok good luck! and have a good day! IP: "+ (IP)
