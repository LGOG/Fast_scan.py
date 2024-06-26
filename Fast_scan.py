import subprocess
import argparse
import re
import signal

# ANSI escape codes for colorizing text
YELLOW = '\033[93m'
GREEN = '\033[92m'
RESET = '\033[0m'

SQL_PORTS = {'3306': 'MySQL', '5432': 'PostgreSQL', '1433': 'MSSQL', '1521': 'Oracle'}

def run_rustscan(ip_address):
    """
    Runs RustScan on the specified IP address to quickly identify open ports.
    """
    print(f"{YELLOW}[~] Starting RustScan on {ip_address}...{RESET}")
    command = ['rustscan', '--ulimit', '5000', '-a', ip_address]
    print(f"{GREEN}[>] {' '.join(command)}{RESET}")
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    return re.findall(r'(\d+)/tcp', result.stdout)

def run_nmap(ip_address, ports):
    """
    Runs Nmap on the specified IP address and ports for detailed scanning.
    """
    print(f"{YELLOW}[~] Starting Nmap deep scan on {ip_address} for ports {ports}...{RESET}")
    command = ['nmap', '-T4', '-A', '-sC', '-p', ports, ip_address]
    print(f"{GREEN}[>] {' '.join(command)}{RESET}")
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    return result.stdout

def find_web_ports(nmap_output):
    """
    Parses Nmap output to find ports serving web content based on service names.
    """
    web_services = re.findall(r'(\d+)/tcp\s+open\s+.*?http\b', nmap_output, re.IGNORECASE)
    return [match.split('/')[0] for match in web_services]

def run_gobuster(ip_address, port):
    """
    Runs Gobuster on the specified IP address and port to enumerate directories.
    """
    user_input = input(f"Do you want to run Gobuster on {ip_address}:{port}? (y/n): ")
    if user_input.lower() in ['y', 'yes']:
        print(f"{YELLOW}[~] Starting Gobuster on {ip_address}:{port}...{RESET}")
        url = f'http://{ip_address}:{port}'
        wordlist = '/usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt'
        command = [
            'gobuster', 'dir', '-w', wordlist, '-t', '25', '--random-agent', '-r',
            '-b', '404,403,429,500,520', '-q', '-u', url
        ]
        print(f"{GREEN}[>] {' '.join(command)}{RESET}")
        subprocess.run(command)

def run_sqlmap(ip_address, port):
    """
    Runs sqlmap on the specified IP address and port if an SQL service is detected.
    """
    print(f"{YELLOW}[~] Starting sqlmap on {ip_address}:{port}...{RESET}")
    command = ['sqlmap', '-u', f'{ip_address}:{port}', '--batch']
    print(f"{GREEN}[>] {' '.join(command)}{RESET}")
    subprocess.run(command)

def main():
    """
    Main function that orchestrates the network scanning process.
    """
    parser = argparse.ArgumentParser(description='Fast Network Scanner')
    parser.add_argument('ip', help='IP address to scan')
    args = parser.parse_args()

    open_ports = run_rustscan(args.ip)
    open_ports = list(set(open_ports))  # Remove duplicates
    ports_str = ','.join(open_ports)

    if open_ports:
        nmap_output = run_nmap(args.ip, ports_str)
        web_ports = find_web_ports(nmap_output)

        for port in web_ports:
            try:
                run_gobuster(args.ip, port)
            except KeyboardInterrupt:
                if port == web_ports[-1]:
                    print(f"{YELLOW}This is the end of the scan.{RESET}")
                    break
                else:
                    print(f"{YELLOW}[-] Gobuster scan interrupted. Moving to next port...{RESET}")
                    continue

        sql_ports = [port for port in open_ports if port in SQL_PORTS.keys()]
        for port in sql_ports:
            run_sqlmap(args.ip, port)

    else:
        print(f"{YELLOW}No ports identified by RustScan. Nmap and Gobuster scans will not be performed.{RESET}")

if __name__ == '__main__':
    main()
