import socket
import platform
import subprocess

def get_network_interfaces():
    """
    Retrieves detailed information about all network interfaces on the system.

    Returns:
        dict: A dictionary containing information about each network interface, including its name, IP address, MAC address, and status.
    """
    os_type = platform.system()
    interfaces = {}

    if os_type == "Linux" or os_type == "Darwin":  # Linux and macOS
        try:
            result = subprocess.check_output(["ifconfig" if os_type == "Darwin" else "ip", "addr"])
            result = result.decode("utf-8").split("\n\n")
            for iface in result:
                lines = iface.splitlines()
                if len(lines) > 1:
                    iface_name = lines[0].split(":")[1].strip()
                    interfaces[iface_name] = {
                        "IP Address": None,
                        "MAC Address": None,
                        "Status": "UP" if "UP" in lines[0] else "DOWN"
                    }
                    for line in lines:
                        if "inet " in line:
                            interfaces[iface_name]["IP Address"] = line.split()[1].split("/")[0]
                        if "ether" in line:
                            interfaces[iface_name]["MAC Address"] = line.split()[1]
        except Exception as e:
            return f"Error retrieving network interfaces on {os_type}: {str(e)}"

    elif os_type == "Windows":
        try:
            result = subprocess.check_output(["ipconfig", "/all"])
            result = result.decode("utf-8").splitlines()
            iface_name = None
            for line in result:
                if line.startswith("Ethernet adapter") or line.startswith("Wireless LAN adapter"):
                    iface_name = line.split(":")[0].strip()
                    interfaces[iface_name] = {
                        "IP Address": None,
                        "MAC Address": None,
                        "Status": "DOWN"
                    }
                if "IPv4 Address" in line or "IPv4" in line:
                    interfaces[iface_name]["IP Address"] = line.split(":")[1].strip().split(" ")[0]
                if "Physical Address" in line:
                    interfaces[iface_name]["MAC Address"] = line.split(":")[1].strip()
                if "Media State" in line and "disconnected" not in line:
                    interfaces[iface_name]["Status"] = "UP"
        except Exception as e:
            return f"Error retrieving network interfaces on Windows: {str(e)}"

    return interfaces

def get_connected_devices(router_ip):
    """
    Retrieves a list of devices connected to the network.

    Args:
        router_ip (str): The IP address of the router.

    Returns:
        list: A list of dictionaries containing information about each connected device (IP address, MAC address, and possibly device name).
    """
    connected_devices = []

    try:
        result = subprocess.check_output(["arp", "-a"])
        result = result.decode("utf-8").splitlines()
        for line in result:
            if router_ip in line:
                continue  # Skip the router itself
            device_info = line.split()
            connected_devices.append({
                "IP Address": device_info[0],
                "MAC Address": device_info[1],
                "Device Name": device_info[2] if len(device_info) > 2 else "Unknown"
            })
    except Exception as e:
        return f"Error retrieving connected devices: {str(e)}"

    return connected_devices

def get_dns_servers():
    """
    Retrieves the DNS servers currently in use by the system.

    Returns:
        list: A list of DNS server IP addresses.
    """
    os_type = platform.system()
    dns_servers = []

    if os_type == "Linux" or os_type == "Darwin":  # Linux and macOS
        try:
            result = subprocess.check_output(["cat", "/etc/resolv.conf"])
            result = result.decode("utf-8").splitlines()
            for line in result:
                if line.startswith("nameserver"):
                    dns_servers.append(line.split()[1])
        except Exception as e:
            return f"Error retrieving DNS servers on {os_type}: {str(e)}"

    elif os_type == "Windows":
        try:
            result = subprocess.check_output(["ipconfig", "/all"])
            result = result.decode("utf-8").splitlines()
            for line in result:
                if "DNS Servers" in line:
                    dns_servers.append(line.split(":")[1].strip())
        except Exception as e:
            return f"Error retrieving DNS servers on Windows: {str(e)}"

    return dns_servers

def get_dhcp_leases():
    """
    Retrieves DHCP lease information, including lease times and assigned IP addresses.

    Returns:
        list: A list of dictionaries containing DHCP lease information.
    """
    os_type = platform.system()
    dhcp_leases = []

    if os_type == "Linux":
        try:
            with open("/var/lib/dhcp/dhclient.leases", "r") as f:
                leases = f.read().split("lease")
                for lease in leases:
                    lease_info = {}
                    for line in lease.splitlines():
                        if "lease" in line:
                            lease_info["IP Address"] = line.split()[1]
                        if "starts" in line:
                            lease_info["Lease Start"] = line.split()[2] + " " + line.split()[3]
                        if "ends" in line:
                            lease_info["Lease End"] = line.split()[2] + " " + line.split()[3]
                    if lease_info:
                        dhcp_leases.append(lease_info)
        except Exception as e:
            return f"Error retrieving DHCP leases on Linux: {str(e)}"

    elif os_type == "Windows":
        try:
            result = subprocess.check_output(["ipconfig", "/all"])
            result = result.decode("utf-8").splitlines()
            lease_info = {}
            for line in result:
                if "Lease Obtained" in line:
                    lease_info["Lease Start"] = line.split(":")[1].strip()
                if "Lease Expires" in line:
                    lease_info["Lease End"] = line.split(":")[1].strip()
                if "IPv4 Address" in line or "IPv4" in line:
                    lease_info["IP Address"] = line.split(":")[1].strip().split(" ")[0]
                    dhcp_leases.append(lease_info)
        except Exception as e:
            return f"Error retrieving DHCP leases on Windows: {str(e)}"

    elif os_type == "Darwin":  # macOS
        return "DHCP lease information retrieval is not supported on macOS."

    return dhcp_leases

def get_router_ip():
    """
    Retrieves the IP address of the default gateway router.

    Returns:
        str: The IP address of the default gateway router.
    """
    os_type = platform.system()

    try:
        if os_type == "Linux":
            result = subprocess.check_output(["ip", "route"])
            result = result.decode("utf-8")
            for line in result.splitlines():
                if "default" in line:
                    return line.split()[2]
        elif os_type == "Darwin":  # macOS
            result = subprocess.check_output(["route", "-n", "get", "default"])
            result = result.decode("utf-8")
            for line in result.splitlines():
                if "gateway" in line:
                    return line.split(":")[1].strip()
        elif os_type == "Windows":
            result = subprocess.check_output(["ipconfig"])
            result = result.decode("utf-8")
            for line in result.splitlines():
                if "Default Gateway" in line:
                    return line.split(":")[1].strip()
    except Exception as e:
        return f"Error retrieving router IP: {str(e)}"

    return "Unsupported operating system."

def get_detailed_network_info():
    """
    Retrieves detailed network information, including network interfaces, connected devices, DNS servers, and DHCP leases.

    Returns:
        dict: A dictionary containing detailed network information.
    """
    router_ip = get_router_ip()
    return {
        "Network Interfaces": get_network_interfaces(),
        "Connected Devices": get_connected_devices(router_ip),
        "DNS Servers": get_dns_servers(),
        "DHCP Leases": get_dhcp_leases(),
    }

# Example usage:
# detailed_network_info = get_detailed_network_info()
# print(detailed_network_info)
