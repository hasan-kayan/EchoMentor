import socket

# Define the range of ports to scan
start_port = 1
end_port = 65535

# Function to scan ports
def scan_ports(start_port, end_port):
    available_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)  # Set timeout to avoid hanging on closed ports

        try:
            # Try to connect to the port
            result = sock.connect_ex(('localhost', port))
            if result == 0:
                available_ports.append(port)
        except socket.error:
            pass
        finally:
            sock.close()

    return available_ports

# Run the port scan
def main():
    print(f"Scanning ports {start_port}-{end_port} on localhost...")
    open_ports = scan_ports(start_port, end_port)

    # Return the results
    return open_ports

# Execute the scan and handle the results
if __name__ == "__main__":
    open_ports = main()

    # Print the results
    if open_ports:
        print(f"Available ports: {open_ports}")
    else:
        print("No available ports found.")
