import subprocess
import os
import time
from colorama import Fore, Style

def create_output_folder(target_url):
    output_folder = "output"
    target_folder = os.path.join(output_folder, target_url)
    
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Create target-specific folder
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    return target_folder

def list_previous_domains(output_folder):
    print(Fore.MAGENTA + "\n--------------------------------------------------------------------------------")
    print(Fore.GREEN + "\n[*] Listing Previous Scanned Domains: \n" + Style.RESET_ALL)
    domains = [folder for folder in os.listdir(output_folder) if os.path.isdir(os.path.join(output_folder, folder))]
    if not domains:
        print("No previous scanned domains.")
    else:
        for domain in domains:
            print(Fore.CYAN + f"- {domain}" + Style.RESET_ALL)
            print(Fore.MAGENTA + "\n--------------------------------------------------------------------------------")

def append_to_file(file_path, content):
    with open(file_path, 'a') as file:
        file.write(content)



def run_whois(target_url, output_folder):
    print(Fore.YELLOW + "[*] Getting Domain Information ..." + Style.RESET_ALL)
    loading_animation()
    whois_command = f"whois {target_url}"
    whois_output = subprocess.run(whois_command, shell=True, capture_output=True, text=True).stdout
    append_to_file(os.path.join(output_folder, f'output_of_{target_url}.txt'), Fore.BLUE + "\n \n \n######################\n \n \n Domain Information:-\n \n \n######################\n \n \n " + Style.RESET_ALL)
    append_to_file(os.path.join(output_folder, f'output_of_{target_url}.txt'), whois_output)
    print(Fore.GREEN + "[*] Scan 1 complete for target: " + target_url + Style.RESET_ALL)

def run_nmap(target_ip, output_folder):
    print(Fore.YELLOW + "[*] Scanning Ports..." + Style.RESET_ALL)
    loading_animation()
    nmap_command = f"nmap {target_ip}"
    nmap_output = subprocess.run(nmap_command, shell=True, capture_output=True, text=True).stdout
    append_to_file(os.path.join(output_folder, f'output_of_{target_url}.txt'), Fore.BLUE + "\n \n \n######################\n \n \n Port Information:-\n \n \n######################\n \n \n " + Style.RESET_ALL)
    append_to_file(os.path.join(output_folder, f'output_of_{target_url}.txt'), nmap_output)
    print(Fore.GREEN + "[*] Scan 2 complete for target: " + target_url + Style.RESET_ALL)

def run_sublist3r(target_url, output_folder):
    print(Fore.YELLOW + "[*] Finding Subdomains ..." + Style.RESET_ALL)
    loading_animation()
    sublist3r_command = f"python3 /opt/Sublist3r/sublist3r.py -d {target_url} -v"
    sublist3r_output = subprocess.run(sublist3r_command, shell=True, capture_output=True, text=True).stdout
    append_to_file(os.path.join(output_folder, f'output_of_{target_url}.txt'), Fore.BLUE + "\n \n \n######################\n \n \n Subdomain Information:-\n \n \n######################\n \n \n " + Style.RESET_ALL)
    append_to_file(os.path.join(output_folder, f'output_of_{target_url}.txt'), sublist3r_output)
    print(Fore.GREEN + "[*] Scan 3 complete for target: " + target_url + Style.RESET_ALL)

def run_wpscan(target_url, output_folder):
    print(Fore.YELLOW + "[*] Finding vuln's via tool 1 ..." + Style.RESET_ALL)
    loading_animation()
    wpscan_command = f"wpscan --url {target_url}"
    wpscan_output = subprocess.run(wpscan_command, shell=True, capture_output=True, text=True).stdout
    append_to_file(os.path.join(output_folder, f'output_of_{target_url}.txt'), Fore.BLUE + "\n \n \n######################\n \n \n Vuln Tool 1 Information:-\n \n \n######################\n \n \n " + Style.RESET_ALL)
    append_to_file(os.path.join(output_folder, f'output_of_{target_url}.txt'), wpscan_output)
    print(Fore.GREEN + "[*] Scan 4 complete for target: " + target_url + Style.RESET_ALL)

def run_nikto(target_url, output_folder):
    print(Fore.YELLOW + "[*] Finding vuln's via tool 2 ..." + Style.RESET_ALL)
    loading_animation()
    nikto_command = f"nikto -h {target_url} -Tuning 123bde -maxtime 1100"
    nikto_output = subprocess.run(nikto_command, shell=True, capture_output=True, text=True).stdout
    append_to_file(os.path.join(output_folder, f'output_of_{target_url}.txt'), Fore.BLUE + "\n \n \n######################\n \n \n Vuln Tool 2 Information:-\n \n \n######################\n \n \n " + Style.RESET_ALL)
    append_to_file(os.path.join(output_folder, f'output_of_{target_url}.txt'), nikto_output)
    print(Fore.GREEN + "[*] Scan 5 complete for target: " + target_url + Style.RESET_ALL)




def custom_ascii_art(message, edition, placeholder):
    ascii_art = r"""
    _________________________________                  _________________________________                  _________________________________
   /                                 \                /                                 \                /                                 \            
  |    ===========================    |              |    ===========================    |              |    ===========================    |
  |   |                           |   |              |   |                           |   |              |   |                           |   |
  |   |   Welcome to Zak's Tool   |   |              |   |   Welcome to Zak's Tool   |   |              |   |   Welcome to Zak's Tool   |   |
  |   |                           |   |              |   |                           |   |              |   |                           |   |
  |   |   - Web Security Edition  |   |              |   |   - Web Security Edition  |   |              |   |   - Web Security Edition  |   |
  |   |                           |   |              |   |                           |   |              |   |                           |   |
  |   |   +++++++++++++++++++++   |   |              |   |   +++++++++++++++++++++   |   |              |   |   +++++++++++++++++++++   |   |
  |   |                           |   |              |   |                           |   |              |   |                           |   |
  |   |   [ -|- ]                 |   |              |   |   ( + /\ + )              |   |              |   |   < %! >                  |   |
  |   |                           |   |              |   |                           |   |              |   |                           |   |
  |   |                           |   |              |   |                           |   |              |   |                           |   |
  |    ===========================    |              |    ===========================    |              |    ===========================    |
  |                                   |              |                                   |              |                                   |
   \_________________________________/                \_________________________________/                \_________________________________/
"""
    for line in ascii_art.split('\n'):
        print(Fore.CYAN + line.format(message, edition, placeholder) + Style.RESET_ALL)
        time.sleep(0.3)  # Adjust the delay as needed

def loading_animation():
    animation_frames = [
        r"""
         __     __ ______   __    __  ______  __        ______   __    __  ______  __     __  __   __  __    __ 
        /  \   /  |      | /  \  /  |/      |/  |      /  __  \ /  |  /  |/      |/  \   /  |/  \ /  |/  |  /  |
       $$  \ /$$/ $$$$$ | $$  \ $$ |$$$$$$/ $$ |      $/$$  \ $$ $$ |  $$ |$$$$$$/ $$  \ /$$/ $$ |$$ |$$ |  $$ |
        $$  /$$/  $$$$$ |  $$  \$$ |  $$ |  $$ |        $$  \__/ $$ |  $$ |  $$ |  $$  /$$/  $$ |$$ |$$ |  $$ |
         $$ $$/   $$$$$ |   $$  $$/   $$ |  $$ |         $$    $$/ $$   $$ |  $$ |   $$ $$/   $$ |$$ |$$ |  $$ |
          $$$/    /$$__ |    $$$$/    $$ |  $$ |_____  __ $$$$$$/   $$$$$$/   $$ |    $$$/    $$ |$$ |$$ \__$$ |
           $/    /$$$$$$ |    $$/     $$/   $$       |/  |$$ |      $$ |      $$/      $$/     $$/ $$/ /$$  $$/ 
                |______/                             $$/ $$/       $$/                                    
    """,
        # Add more frames as needed
    ]

    for frame in animation_frames:
        for line in frame.split('\n'):
            print(Fore.MAGENTA + line + Style.RESET_ALL)
            time.sleep(0.3)  # Adjust the delay as needed

if __name__ == "__main__":
    custom_ascii_art("Initializing", "Web Security Edition", "{}")
    loading_animation()
    
    while True:
        print(Fore.BLUE + "\nOptions:")
        print(Fore.GREEN + "1. List Previous Scanned Domains" + Style.RESET_ALL)
        print(Fore.YELLOW + "2. Scan New Domain" + Style.RESET_ALL)
        print(Fore.RED + "3. Exit" + Style.RESET_ALL)

        option = input(Fore.CYAN + "Select an option: " + Style.RESET_ALL)

        if option == '1':
            output_folder = "output"
            list_previous_domains(output_folder)
        elif option == '2':
            target_url = input(Fore.CYAN + "Enter the new target URL: " + Style.RESET_ALL)
            output_folder = create_output_folder(target_url)
            target_ip = os.popen(f"host {target_url} | grep 'has address' | awk '{{print $4}}'").read().strip()

            append_to_file(os.path.join(output_folder, f'output_of_{target_url}.txt'), Fore.MAGENTA + f"\n\n\n \n \n######################\n \n \n Scanning Target: {target_url}\n \n \n######################\n \n \n " + Style.RESET_ALL)
            
            run_whois(target_url, output_folder)
            run_nmap(target_ip, output_folder)
            run_sublist3r(target_url, output_folder)
            run_wpscan(target_url, output_folder)
            run_nikto(target_url, output_folder)

            print(Fore.CYAN + "[*] Scanning complete for target: " + target_url + Style.RESET_ALL)
        elif option.lower() == '3':
            print(Fore.RED + "Exiting the program ......" + Style.RESET_ALL)
            break
        else:
            print("\n" + Fore.YELLOW + "Invalid option. Please select a valid option." + Style.RESET_ALL)
