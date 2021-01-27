😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵                                                                                   

This script uses the fast scan of rustscan with the deep scan of nmap and at the end, if it finds any web server open it will gobuster it as well!
Make sure that you have all in order for it to work

https://github.com/RustScan/RustScan

https://github.com/nmap/nmap

https://github.com/OJ/gobuster

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

first:
chmod +x Fast_scan.py

how to use:
python3 Fast_scan.py

put the IP you want to scan and let it run :)

If it will find any webserver just say yes or no for gobuster

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

How does it work?
It uses rustscan on all 6535 ports.
It returns a list of open ports.
Then it takes the list and uses it with nmap.
If any webserver are oprn it will ask you if you want to scan it as well

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

nmap -sV -A -p- -sC <IP> - Will take you 20 minutes to scan all 6535 ports.

Same scan with Fast_scan.py will take you 2 minutes!

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

If you stop the nmap scan with "CTRL+C" but rustscan found a webserver you will still run gobuster

😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵
