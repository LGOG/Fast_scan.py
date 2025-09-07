# Fast Network Scanner

## Overview

`Fast_scan.py` is an **advanced network scanning tool** written in Python that automates the discovery of vulnerabilities in network services. It orchestrates a powerful sequence of external tools, including **RustScan**, **Nmap**, **Nikto**, **Gobuster**, and **sqlmap**, to provide a comprehensive and efficient security assessment. This tool is designed for cybersecurity professionals and enthusiasts seeking a streamlined workflow for network and web application security testing.

## Prerequisites

To use `Fast_scan.py` successfully, ensure the following command-line tools are installed on your system.

### RustScan

RustScan is used for rapid port discovery.

```bash
# Download and install RustScan
wget https://github.com/RustScan/RustScan/releases/download/1.8.0/rustscan_1.8.0_amd64.deb
sudo dpkg -i rustscan_1.8.0_amd64.deb
```

### Nmap

Nmap is essential for in-depth service and version analysis.

```bash
# Install Nmap
sudo apt update
sudo apt install nmap
```

### Nikto

Nikto is a web server scanner that identifies vulnerabilities and misconfigurations.

```bash
# Install Nikto
sudo apt update
sudo apt install nikto
```

### Gobuster

Gobuster is used for web directory enumeration.

```bash
# Install Gobuster
sudo apt update
sudo apt install gobuster
```

### sqlmap

sqlmap is an automatic tool for detecting and exploiting SQL injection flaws.

```bash
# Install sqlmap
sudo apt update
sudo apt install sqlmap
```

### smbclient

smbclient is used for interacting with SMB/CIFS servers.

```bash
# Install smbclient
sudo apt update
sudo apt install smbclient
```

-----

## Usage

1.  **Run the Script**: Execute the script using Python 3, providing the target IP address as an argument.

    ```bash
    python3 Fast_scan.py <target-IP>
    ```

2.  **Save Output**: To save the scan results to a file, use the `-o` or `--output` flag.

    ```bash
    python3 Fast_scan.py <target-IP> -o <filename>
    ```

3.  **Interactive Prompts**: The script will prompt you before running more intensive scans, such as Nikto, Gobuster, smbclient, and sqlmap, allowing you to control the scanning process dynamically.

4.  **View Results**: The output will be displayed in the terminal and saved to the specified output file, if provided. The report is structured in the following order:

      * **RustScan**: Fast port scan results.
      * **Nmap**: Detailed service and version information for discovered ports.
      * **SMBclient**: Enumeration of SMB shares (if ports 139 or 445 are open).
      * **Nikto**: Web vulnerability scan (if HTTP/S services are detected).
      * **Gobuster**: Directory brute-forcing results (if HTTP/S services are detected).
      * **sqlmap**: SQL injection testing (if common SQL ports are open).

-----

## Features

  * **Rapid Port Scanning**: Utilizes **RustScan** for ultra-fast port discovery, saving significant time in the initial recon phase.
  * **Comprehensive Service Analysis**: Integrates **Nmap** to provide in-depth service and version detection on open ports.
  * **Web Vulnerability Scanning**: Automatically runs **Nikto** to identify common web server vulnerabilities.
  * **Web Enumeration**: Seamlessly integrates **Gobuster** to enumerate web directories and hidden files on discovered web servers.
  * **SQL Injection Testing**: Automatically invokes **sqlmap** to check for potential SQL injection vulnerabilities on detected database ports.
  * **SMB Share Enumeration**: Scans for and enumerates SMB shares using **smbclient**, enhancing the scope of network assessment.
  * **Interactive Control**: Provides interactive prompts to selectively run more aggressive scans, giving users granular control over the process.
  * **Persistent Logging**: The optional `-o` flag allows all scan output to be saved to a file, creating a detailed record of the assessment.

-----

## Disclaimer

`Fast_scan.py` is intended for **lawful and ethical cybersecurity activities**. Users are solely responsible for ensuring they have explicit permission to scan the networks and systems they target. The creator and contributors of this script assume no liability for misuse or any legal consequences arising from its use.
