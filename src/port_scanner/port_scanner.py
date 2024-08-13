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
print(f"Scanning ports {start_port}-{end_port} on localhost...")
open_ports = scan_ports(start_port, end_port)

# Print the results
if open_ports:
    print(f"Available ports: {open_ports}")
else:
    print("No available ports found.")

# Save the results to a file
with open('available_ports.txt', 'w') as f:
    for port in open_ports:
        f.write(f"{port}\n")

print("Scan complete. Results saved to 'available_ports.txt'.")
