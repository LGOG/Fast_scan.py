This script, Fast_scan.py, streamlines the process of conducting comprehensive network scans. It employs RustScan to quickly identify open ports on a target IP address, then passes these findings to Nmap for an in-depth analysis. If web servers are detected, the script optionally employs Gobuster to perform directory enumeration. This tool is designed to assist cybersecurity professionals and enthusiasts in efficiently assessing network vulnerabilities.

Prerequisites
Before using Fast_scan.py, ensure the following tools are installed on your system:

RustScan
Download and install RustScan:
bash
Copy code
wget https://github.com/RustScan/RustScan/releases/download/1.8.0/rustscan_1.8.0_amd64.deb
dpkg -i rustscan_1.8.0_amd64.deb
Gobuster
Install Gobuster using apt:
sql
Copy code
sudo apt update && sudo apt install gobuster
Nmap
Install Nmap using apt:
sql
Copy code
sudo apt update && sudo apt-get install nmap
Usage
Run the Script: Execute the script with Python 3:

Copy code
python3 Fast_scan.py
Input Target IP: When prompted, enter the IP address you wish to scan.

View Results: The script will display the scanning results directly in the terminal.

RustScan: Initial fast port scanning.
Nmap: Detailed scan based on RustScan results.
Gobuster: Optional web server directory enumeration.
Features
Fast Port Scanning: Utilizes RustScan for rapid port scanning, significantly reducing the time to identify open ports.
Comprehensive Analysis: Leverages Nmap's capabilities for a thorough investigation of the discovered ports, providing detailed insights into the network's security posture.
Web Server Enumeration: Offers the option to run Gobuster for directory enumeration on detected web servers, aiding in the discovery of potential web-based vulnerabilities.
Customization
Modify Nmap and Gobuster parameters within the script to tailor the scan to your specific requirements.
Note
The script includes emoji and other unicode characters for visual emphasis, which should be compatible with most terminal applications.
Disclaimer
The Fast_scan.py script is intended for lawful cybersecurity activities. Users should only scan networks and systems they are authorized to analyze. The creator of this script assumes no liability for misuse or any legal repercussions that arise from using the tool.
