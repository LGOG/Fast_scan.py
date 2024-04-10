# Fast Network Scanner

## Overview

`Fast_scan.py` is an advanced network scanning tool designed to automate identifying vulnerabilities in network services. It integrates RustScan, Nmap, Gobuster, and now sqlmap to provide a comprehensive view of network security posture. RustScan is used for rapid port discovery, Nmap for detailed service analysis, Gobuster for web directory enumeration, and sqlmap for detecting SQL injection vulnerabilities. This tool is invaluable for cybersecurity professionals and enthusiasts seeking to conduct thorough network assessments efficiently.

## Prerequisites

Before using `Fast_scan.py,` ensure you have the following tools installed on your system:

### RustScan

- Download and install RustScan:
  ```
  wget https://github.com/RustScan/RustScan/releases/download/1.8.0/rustscan_1.8.0_amd64.deb
  dpkg -i rustscan_1.8.0_amd64.deb
  ```

### Gobuster

- Install Gobuster using apt:
  ```
  sudo apt update && sudo apt install gobuster
  ```

### Nmap

- Install Nmap using apt:
  ```
  sudo apt update && sudo apt-get install nmap
  ```

### sqlmap

- Install sqlmap (if not already installed):
  ```
  sudo apt install sqlmap
  ```

## Usage

1. **Run the Script**: Execute the script with Python 3:
   ```
   python3 Fast_scan.py <target-IP>
   ```

2. **View Results**: The script will display the scanning results directly in the terminal, including:

   - **RustScan**: Initial fast port scanning.
   - **Nmap**: Detailed service analysis based on RustScan results.
   - **Gobuster**: Optional directory enumeration on detected web servers.
   - **sqlmap**: Automated testing for SQL injection vulnerabilities on identified SQL services.

## Features

- **Fast Port Scanning**: Uses RustScan for quick identification of open ports, streamlining the initial phase of network scanning.
- **Comprehensive Analysis**: Employs Nmap for in-depth analysis of services running on the open ports, providing detailed security insights.
- **Web Server Enumeration**: Integrates Gobuster for optional directory enumeration, helping uncover potential web vulnerabilities.
- **SQL Vulnerability Detection**: Adds sqlmap to automatically test for SQL injection vulnerabilities on recognized SQL service ports, enhancing database security assessment.

## Customization

- Adjust Nmap, Gobuster, and sqlmap parameters within the script to customize the scanning process according to specific requirements.

## Why Use Fast Network Scanner?

Using `Fast_scan.py` allows cybersecurity professionals to conduct a multi-faceted network assessment easily. It combines the strengths of leading security tools into a single, streamlined process, enabling users to:

- Rapidly identify and analyze open ports.
- Perform detailed service and vulnerability scans.
- Enumerate web directories for hidden resources.
- Detect and assess potential SQL injection points.

This integrated approach saves time and enhances the analytical depth, making it a powerful tool for proactive security assessments and penetration testing.

## Disclaimer

`Fast_scan.py` is intended for lawful cybersecurity activities. Users should only scan networks and systems they are authorized to analyze. The creator of this script assumes no liability for misuse or any legal repercussions that arise from using the tool.
