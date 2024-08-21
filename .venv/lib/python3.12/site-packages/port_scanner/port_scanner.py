import socket

def scan_ports(start_port, end_port):
    """
    Scans a range of ports on the localhost and returns a list of open ports.

    Args:
        start_port (int): The starting port number.
        end_port (int): The ending port number.

    Returns:
        list: A list of open ports within the specified range.
    """
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

def main(start_port, end_port):
    """
    Executes the port scan on localhost.

    Args:
        start_port (int): The starting port number.
        end_port (int): The ending port number.

    Returns:
        list: A list of open ports within the specified range.
    """
    print(f"Scanning ports {start_port}-{end_port} on localhost...")
    open_ports = scan_ports(start_port, end_port)

    return open_ports
