import subprocess
import argparse
import re
import signal
import sys
import datetime

# ANSI escape codes for colorizing text
YELLOW = '\033[93m'
GREEN = '\033[92m'
RESET = '\033[0m'
RED = '\033[91m'

SQL_PORTS = {'3306': 'MySQL', '5432': 'PostgreSQL', '1433': 'MSSQL', '1521': 'Oracle'}
SMB_PORTS = ['139', '445']

def print_to_console_and_file(file, message):
    """
    Prints a message to both the console and a specified file.
    """
    print(message, end='', file=sys.stdout, flush=True)
    if file:
        print(message, end='', file=file, flush=True)

def run_rustscan(ip_address, output_file):
    """
    Runs RustScan on the specified IP address to quickly identify open ports.
    """
    print_to_console_and_file(output_file, f"{YELLOW}[~] Starting RustScan on {ip_address}...{RESET}\n")
    command = ['rustscan', '--ulimit', '5000', '-a', ip_address]
    print_to_console_and_file(output_file, f"{GREEN}[>] {' '.join(command)}{RESET}\n")
    result = subprocess.run(command, capture_output=True, text=True)
    print_to_console_and_file(output_file, result.stdout)
    return re.findall(r'(\d+)/tcp', result.stdout)

def run_nmap(ip_address, ports, output_file):
    """
    Runs Nmap on the specified IP address and ports for detailed scanning.
    """
    print_to_console_and_file(output_file, f"{YELLOW}[~] Starting Nmap deep scan on {ip_address} for ports {ports}...{RESET}\n")
    command = ['nmap', '-T4', '-A', '-sC', '-p', ports, ip_address]
    print_to_console_and_file(output_file, f"{GREEN}[>] {' '.join(command)}{RESET}\n")
    result = subprocess.run(command, capture_output=True, text=True)
    print_to_console_and_file(output_file, result.stdout)
    return result.stdout

def find_web_ports(nmap_output):
    """
    Parses Nmap output to find ports serving web content based on service names.
    """
    web_services = re.findall(r'(\d+)/tcp\s+open\s+.*?http(?:s)?\b', nmap_output, re.IGNORECASE)
    return [match.split('/')[0] for match in web_services]

def run_smbclient(ip_address, output_file):
    """
    Runs smbclient on the specified IP address to enumerate SMB shares.
    """
    user_input = input(f"Do you want to run smbclient on {ip_address}? (Y/n): ")
    if user_input.lower() in ['y', 'yes', '']:
        print_to_console_and_file(output_file, f"{YELLOW}[~] Starting smbclient on {ip_address}...{RESET}\n")
        command = ['smbclient', '-L', f'//{ip_address}', '--no-pass']
        print_to_console_and_file(output_file, f"{GREEN}[>] {' '.join(command)}{RESET}\n")

        if output_file:
            with open(output_file.name, 'a') as f:
                subprocess.run(command, stdout=f, stderr=f)
        else:
            subprocess.run(command)

def run_nikto(ip_address, port, output_file):
    """
    Runs Nikto on the specified IP address and port to scan for web server vulnerabilities.
    """
    user_input = input(f"Do you want to run Nikto on http://{ip_address}:{port}? (Y/n): ")
    if user_input.lower() in ['y', 'yes', '']:
        print_to_console_and_file(output_file, f"{YELLOW}[~] Starting Nikto on {ip_address}:{port}...{RESET}\n")
        url = f'http://{ip_address}:{port}'
        command = ['nikto', '-h', url]
        print_to_console_and_file(output_file, f"{GREEN}[>] {' '.join(command)}{RESET}\n")
        
        if output_file:
            with open(output_file.name, 'a') as f:
                subprocess.run(command, stdout=f, stderr=f)
        else:
            subprocess.run(command)

def run_gobuster(ip_address, port, output_file):
    """
    Runs Gobuster on the specified IP address and port to enumerate directories.
    """
    user_input = input(f"Do you want to run Gobuster on {ip_address}:{port}? (Y/n): ")
    if user_input.lower() in ['y', 'yes', '']:
        print_to_console_and_file(output_file, f"{YELLOW}[~] Starting Gobuster on {ip_address}:{port}...{RESET}\n")
        url = f'http://{ip_address}:{port}'
        wordlist = '/usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt'
        command = [
            'gobuster', 'dir', '-w', wordlist, '-t', '25', '--random-agent', '-r',
            '-b', '404,403,429,500,520', '-q', '-u', url
        ]
        print_to_console_and_file(output_file, f"{GREEN}[>] {' '.join(command)}{RESET}\n")
        
        if output_file:
            with open(output_file.name, 'a') as f:
                subprocess.run(command, stdout=f, stderr=f)
        else:
            subprocess.run(command)

def run_sqlmap(ip_address, port, output_file):
    """
    Runs sqlmap on the specified IP address and port if an SQL service is detected.
    """
    user_input = input(f"Do you want to run sqlmap on {ip_address}:{port}? (Y/n): ")
    if user_input.lower() in ['y', 'yes', '']:
        print_to_console_and_file(output_file, f"{YELLOW}[~] Starting sqlmap on {ip_address}:{port}...{RESET}\n")
        command = ['sqlmap', '-u', f'{ip_address}:{port}', '--batch']
        print_to_console_and_file(output_file, f"{GREEN}[>] {' '.join(command)}{RESET}\n")
        
        if output_file:
            with open(output_file.name, 'a') as f:
                subprocess.run(command, stdout=f, stderr=f)
        else:
            subprocess.run(command)

def main():
    """
    Main function that orchestrates the network scanning process.
    """
    parser = argparse.ArgumentParser(description='Fast Network Scanner')
    parser.add_argument('ip', help='IP address to scan')
    parser.add_argument('-o', '--output', help='Save output to a file', metavar='FILENAME')
    args = parser.parse_args()

    output_file = None
    if args.output:
        try:
            output_file = open(args.output, 'w')
            print_to_console_and_file(output_file, f"{RED}[!] Output will be saved to {args.output}{RESET}\n")
            output_file.write(f"Scan results for IP: {args.ip}\n")
            output_file.write(f"Scan started at: {datetime.datetime.now()}\n\n")
        except IOError:
            print(f"{RED}[-] Error: Could not open file {args.output} for writing. Exiting.{RESET}")
            sys.exit(1)
    else:
        print(f"{RED}[!] To save the output, use the -o or --output flag: python your_script.py <IP> -o <filename>{RESET}\n")

    try:
        open_ports = run_rustscan(args.ip, output_file)
        open_ports = list(set(open_ports))
        ports_str = ','.join(open_ports)

        if open_ports:
            nmap_output = run_nmap(args.ip, ports_str, output_file)
            web_ports = find_web_ports(nmap_output)
            
            # Check for SMB ports and run smbclient if found
            smb_ports = [port for port in open_ports if port in SMB_PORTS]
            if smb_ports:
                run_smbclient(args.ip, output_file)

            for port in web_ports:
                try:
                    run_nikto(args.ip, port, output_file)
                    run_gobuster(args.ip, port, output_file)
                except KeyboardInterrupt:
                    if port == web_ports[-1]:
                        print_to_console_and_file(output_file, f"{YELLOW}This is the end of the scan.{RESET}\n")
                        break
                    else:
                        print_to_console_and_file(output_file, f"{YELLOW}[-] Scan interrupted. Moving to next port...{RESET}\n")
                        continue

            sql_ports = [port for port in open_ports if port in SQL_PORTS.keys()]
            for port in sql_ports:
                run_sqlmap(args.ip, port, output_file)
        else:
            print_to_console_and_file(output_file, f"{YELLOW}No ports identified by RustScan. Nmap and other scans will not be performed.{RESET}\n")

    finally:
        if output_file:
            output_file.write(f"\nScan finished at: {datetime.datetime.now()}\n")
            output_file.close()

if __name__ == '__main__':
    main()
