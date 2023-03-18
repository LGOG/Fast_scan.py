This script will scan a host using the fastest, [Rustscan] first, then it will move the results over to Nmap for a deep scan, and at the end, if it finds any web server, it will scan it as well using Gobuster
Before you can use this script, make sure that you have the following:

**Rustscan installed:**
1. wget https://github.com/RustScan/RustScan/releases/download/1.8.0/rustscan_1.8.0_amd64.deb
2. dpkg -i rustscan_1.8.0_amd64.deb

**Gobuster installed:**
sudo apt update && sudo apt install gobuster

**Nmap installed:**
sudo apt update && sudo apt-get install nmap

You can now run this script.
python3 Fast_scan.py
