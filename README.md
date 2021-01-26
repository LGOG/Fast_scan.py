# Fast_scan.py

This script uses the fast scan of rustscan with the deep scan of nmap
Make sure that you have both in order for it to work

https://github.com/RustScan/RustScan

https://github.com/nmap/nmap


first:
chmod +x Fast_scan.py

how to use:
python3 Fast_scan.py

put the IP you want to scan and let it run :)

How does it work?
It uses rustscan on all 6535 ports.
It returns a list of open ports.
Then it takes the list and uses it with nmap.


nmap -sV -A -p- -sC <IP> - Will take you 20 minutes to scan all 6535 ports.
 
Same scan with Fast_scan.py will take you 2 minutes!
