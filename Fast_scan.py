import subprocess
import argparse
import re

# ANSI escape codes for colorizing text
YELLOW = '\033[93m'  # Yellow color
GREEN = '\033[92m'   # Green color
RESET = '\033[0m'    # Reset color to default

def run_rustscan(ip_address):
    # Runs RustScan on the specified IP address to quickly identify open ports.
    print(f"{YELLOW}[~] Starting RustScan on {ip_address}...{RESET}")
    command = ['rustscan', '--ulimit', '5000', '-a', ip_address]
    print(f"{GREEN}[>] {' '.join(command)}{RESET}")  # Print the full command syntax
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    # Extract and return open port numbers from the RustScan output
    return re.findall(r'(\d+)/tcp', result.stdout)

def run_nmap(ip_address, ports):
    # Runs Nmap on the specified IP address and ports for detailed scanning.
    print(f"{YELLOW}[~] Starting Nmap deep scan on {ip_address} for ports {ports}...{RESET}")
    command = ['nmap', '-T4', '-sC', '-p', ports, ip_address]
    print(f"{GREEN}[>] {' '.join(command)}{RESET}")  # Print the full command syntax
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    return result.stdout

def find_web_ports(nmap_output):
    #Parses Nmap output to find ports serving web content based on service names.
    Considers any service containing 'http' as a web service.
    web_services = re.findall(r'(\d+)/tcp open\s+([\w-]+)', nmap_output)
    return [port for port, service in web_services if 'http' in service]
    
def run_gobuster(ip_address, port):
    # Runs Gobuster on the specified IP address and port to enumerate directories,
    after asking the user for confirmation.
    user_input = input(f"Do you want to run Gobuster on {ip_address}:{port}? (y/n): ")
    if user_input.lower() in ['y', 'yes']:
        print(f"{YELLOW}[~] Starting Gobuster on {ip_address}:{port} with specified blacklist status codes...{RESET}")
        url = f'http://{ip_address}:{port}'
        wordlist = '/usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt'
        command = [
            'gobuster', 'dir', '-w', wordlist, '-t', '25', '--random-agent', '-r',
            '-b', '404,403,429,500,520', '-q', '-u', url
        ]
        print(f"{GREEN}[>] {' '.join(command)}{RESET}")  # Print the full command syntax
        subprocess.run(command)

def main():
    # Main function that orchestrates the network scanning process.
    parser = argparse.ArgumentParser(description='Fast Network Scanner')
    parser.add_argument('ip', help='IP address to scan')
    args = parser.parse_args()

    open_ports = run_rustscan(args.ip)
    open_ports = list(set(open_ports))  # Remove duplicates
    ports_str = ','.join(open_ports)

    if open_ports:
        nmap_output = run_nmap(args.ip, ports_str)
        web_ports = find_web_ports(nmap_output)

        for port in open_ports:  # Iterate over all open ports obtained from RustScan
            if port in web_ports:
                run_gobuster(args.ip, port)
    else:
        print("No ports identified by RustScan. Nmap and Gobuster scans will not be performed.")

if __name__ == '__main__':
    main()
