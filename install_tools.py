import subprocess
import os
import sys

def install_tools():
    try:
        # Update package list
        print("[*] Updating package list...")
        subprocess.run(["sudo", "apt-get", "update"], check=True)

        # Install whois, nmap, nikto, ruby, and ruby-dev
        print("[*] Installing whois, nmap, nikto, ruby, and ruby-dev...")
        subprocess.run(["sudo", "apt-get", "install", "-y", "whois", "nmap", "nikto", "ruby", "ruby-dev"], check=True)

        # Clone Sublist3r repository
        print("[*] Cloning Sublist3r repository...")
        if not os.path.exists("/opt/Sublist3r"):
            subprocess.run(["sudo", "git", "clone", "https://github.com/aboul3la/Sublist3r.git", "/opt/Sublist3r"], check=True)

        # Install Sublist3r dependencies
        print("[*] Installing Sublist3r dependencies...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "/opt/Sublist3r/requirements.txt"], check=True)

        # Install WPScan via RubyGems
        print("[*] Installing WPScan...")
        subprocess.run(["sudo", "gem", "install", "wpscan"], check=True)

        print("[*] All tools installed successfully!")

    except subprocess.CalledProcessError as e:
        print(f"[!] An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_tools()
