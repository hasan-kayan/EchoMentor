import socket
import uuid
import requests
import os

# Function to get the local IP address
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        # Doesn't need to actually connect
        s.connect(('8.8.8.8', 1))
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = '127.0.0.1'
    finally:
        s.close()
    return local_ip

# Function to get the MAC address
def get_mac_address():
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
                    for elements in range(0, 2*6, 8)][::-1])
    return mac

# Function to get the public IP address
def get_public_ip():
    try:
        public_ip = requests.get('https://api.ipify.org').text
    except Exception:
        public_ip = 'Unable to retrieve'
    return public_ip

# Function to create a URL for remote connections
def create_remote_url(public_ip, port=8080):
    url = f"http://{public_ip}:{port}/"
    return url

# Logging the network details
def log_network_details():
    local_ip = get_local_ip()
    mac_address = get_mac_address()
    public_ip = get_public_ip()
    remote_url = create_remote_url(public_ip)

    # Prepare log file
    log_file = "network_details.txt"
    with open(log_file, 'w') as f:
        f.write(f"Local IP Address: {local_ip}\n")
        f.write(f"MAC Address: {mac_address}\n")
        f.write(f"Public IP Address: {public_ip}\n")
        f.write(f"Remote Connection URL: {remote_url}\n")

    print(f"Network details logged to {log_file}")
    print(f"Local IP Address: {local_ip}")
    print(f"MAC Address: {mac_address}")
    print(f"Public IP Address: {public_ip}")
    print(f"Remote Connection URL: {remote_url}")

# Run the function to log network details
log_network_details()
