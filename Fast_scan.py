#!/usr/bin/pyhton

import os

print ("LG_OG")
print (" ")

IP = input("IP:? ")

x = os.popen('rustscan -a '+IP).read()
c = x.split()
rust = c[153::]

port_numbers = []

#Takes only the ports
a = [i for i,x in enumerate(rust) if x == "port"]
for port in a:
	port_numbers.append(rust[port+1])

#takes only the numbers 
open_ports = []
for i in port_numbers:
    open_ports.append(i.split('/')[0])


#remove "" and spaces
For_nmap = (','.join(open_ports))

#If you want to change the nmap options do it here
#os.system ('nmap -A -<Add> -<change> -p ' + (For_nmap) + " " +(IP) )
os.system ('nmap -sC -p ' + (For_nmap) + " " +(IP) )

print ("LG_OG")
print (" ")

