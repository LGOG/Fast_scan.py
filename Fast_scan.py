#!/usr/bin/pyhton

import os


print ("😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵")

IP = input("IP:? ")

rust_input = os.popen('rustscan -a '+IP).read()
c = rust_input.split()
rust = c[153::]

print (rust_input)

port_numbers = []

#Takes only the port
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
os.system ('nmap -sV -A -sC -p ' + (For_nmap) + " " +(IP))

print ("The ip was: " + IP)
