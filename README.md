# VulnSweep

VulnSweep is an automated web security assessment tool designed to help you identify vulnerabilities across your web assets. By combining various powerful scanning techniques, VulnSweep simplifies the process of securing your online presence. Whether you're a seasoned security professional or new to the field, this tool offers a user-friendly way to stay ahead of potential threats.

# Features

Domain Information Retrieval: Gather domain registration details using whois.
Port Scanning: Discover open ports and services on a target using nmap.
Subdomain Discovery: Identify subdomains associated with your target using Sublist3r.
Vulnerability Scanning: Scan for vulnerabilities using WPScan and Nikto.
Organized Output: All scan results are saved in a structured directory, making it easy to review and analyze findings.



# Output
![image](https://github.com/user-attachments/assets/7b95c29f-adeb-4410-93a7-5f6b34988bb1)



# Usage
```bash
python3 vulnsweep.py
```

# Setup
## Prerequisites
Before running VulnSweep, ensure that you have the following installed on your system:

Python 3.x: The script is written in Python, so you'll need Python 3 installed.
```bash
sudo apt-get install python3
```

whois: A command-line utility for retrieving domain registration information.
```bash
sudo apt-get install whois
```

nmap: A network scanning tool used to discover hosts and services on a computer network.
```bash
sudo apt-get install nmap
```

Sublist3r: A subdomain enumeration tool written in Python.
Clone the repository and install dependencies:
```bash
git clone https://github.com/aboul3la/Sublist3r.git /opt/Sublist3r
pip install -r /opt/Sublist3r/requirements.txt
```

WPScan: A WordPress security scanner.
```bash
sudo gem install wpscan
```

Nikto: A web server scanner that performs comprehensive tests against web servers.
```bash
sudo apt-get install nikto
```

Thanks to the developers of whois, nmap, Sublist3r, WPScan, and Nikto for creating such powerful tools.
