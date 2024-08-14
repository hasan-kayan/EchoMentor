import socket
import platform
import subprocess
import os

# Function to check Wi-Fi encryption type
def check_wifi_encryption():
    """
    Checks the Wi-Fi encryption type and returns the SSID and security type.

    Returns:
        str: A string containing the SSID and security type of the Wi-Fi connection.

    Raises:
        Exception: If there is an error checking the Wi-Fi encryption.

    """
    os_type = platform.system()

    if os_type == "Linux":
        try:
            result = subprocess.check_output(['nmcli', '-f', 'active,ssid,security', 'dev', 'wifi'])
            result = result.decode('utf-8')
            wifi_info = [line.split() for line in result.splitlines() if 'yes' in line]

            if not wifi_info:
                return "No Wi-Fi connection found."

            ssid = wifi_info[0][1]
            security = wifi_info[0][2] if len(wifi_info[0]) > 2 else "Open"

            return f"SSID: {ssid}, Security: {security}"
        except Exception as e:
            return f"Error checking Wi-Fi encryption on Linux: {str(e)}"

    elif os_type == "Darwin":  # macOS
        try:
            result = subprocess.check_output(
                ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-I"]
            )
            result = result.decode('utf-8')
            security_type = None
            ssid = None

            for line in result.splitlines():
                if "SSID" in line:
                    ssid = line.split(":")[1].strip()
                if "link auth" in line:
                    security_type = line.split(":")[1].strip()

            if ssid and security_type:
                return f"SSID: {ssid}, Security: {security_type}"
            else:
                return "Could not determine Wi-Fi encryption."
        except Exception as e:
            return f"Error checking Wi-Fi encryption on macOS: {str(e)}"

    elif os_type == "Windows":
        try:
            result = subprocess.check_output(["netsh", "wlan", "show", "interfaces"])
            result = result.decode('utf-8')
            ssid = None
            security_type = None

            for line in result.splitlines():
                if "SSID" in line:
                    ssid = line.split(":")[1].strip()
                if "Authentication" in line:
                    security_type = line.split(":")[1].strip()

            if ssid and security_type:
                return f"SSID: {ssid}, Security: {security_type}"
            else:
                return "Could not determine Wi-Fi encryption."
        except Exception as e:
            return f"Error checking Wi-Fi encryption on Windows: {str(e)}"

    return "Unsupported operating system."

# Function to scan router ports
def scan_router_ports(router_ip, start_port=1, end_port=1024):
    """
    Scans the specified range of ports on a router to check for open ports.

    Args:
        router_ip (str): The IP address of the router to scan.
        start_port (int, optional): The starting port number of the scan range. Defaults to 1.
        end_port (int, optional): The ending port number of the scan range. Defaults to 1024.

    Returns:
        list: A list of open ports found during the scan.
    """
    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)  # Set timeout to avoid hanging on closed ports

        try:
            result = sock.connect_ex((router_ip, port))
            if result == 0:
                open_ports.append(port)
        except socket.error:
            pass
        finally:
            sock.close()

    return open_ports

# Function to find router IP address
def get_router_ip():
    """
    Retrieves the IP address of the default gateway router.

    Returns:
        str: The IP address of the default gateway router.

    Raises:
        Exception: If there is an error retrieving the router IP.
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

# Function to check if SSID is hidden
def check_ssid_hidden():
    """
    Check the hidden status of the SSID for the current Wi-Fi connection.

    Returns:
        str: A string indicating the SSID and its hidden status.

    Raises:
        Exception: If there is an error checking the SSID hidden status.

    """
    os_type = platform.system()

    if os_type == "Linux":
        try:
            result = subprocess.check_output(['nmcli', '-f', 'active,ssid,hidden', 'dev', 'wifi'])
            result = result.decode('utf-8')
            wifi_info = [line.split() for line in result.splitlines() if 'yes' in line]

            if not wifi_info:
                return "No Wi-Fi connection found."

            ssid = wifi_info[0][1]
            hidden = wifi_info[0][2] if len(wifi_info[0]) > 2 else "no"

            return f"SSID: {ssid}, Hidden: {hidden}"
        except Exception as e:
            return f"Error checking SSID hidden status on Linux: {str(e)}"

    elif os_type == "Darwin":  # macOS
        try:
            result = subprocess.check_output(
                ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-I"]
            )
            result = result.decode('utf-8')
            ssid = None

            for line in result.splitlines():
                if "SSID" in line:
                    ssid = line.split(":")[1].strip()

            if ssid:
                return f"SSID: {ssid}, Hidden: No"  # macOS does not provide direct hidden SSID information through this method
            else:
                return "SSID is hidden or could not be detected."
        except Exception as e:
            return f"Error checking SSID hidden status on macOS: {str(e)}"

    elif os_type == "Windows":
        try:
            result = subprocess.check_output(["netsh", "wlan", "show", "interfaces"])
            result = result.decode('utf-8')
            ssid = None

            for line in result.splitlines():
                if "SSID" in line:
                    ssid = line.split(":")[1].strip()

            if ssid:
                return f"SSID: {ssid}, Hidden: No"  # Windows does not directly indicate hidden SSID status
            else:
                return "SSID is hidden or could not be detected."
        except Exception as e:
            return f"Error checking SSID hidden status on Windows: {str(e)}"

    return "Unsupported operating system."

# Function to check for weak or default passwords (simple check)
def check_default_passwords(router_ip):
    """
    Checks if the router has a web interface with default credentials on common ports.

    Args:
        router_ip (str): The IP address of the router.

    Returns:
        str: A message indicating whether a web interface with default credentials is detected on common ports or not.
    """
    common_ports = [80, 443, 8080, 8443]
    open_ports = scan_router_ports(router_ip, start_port=min(common_ports), end_port=max(common_ports))

    if any(port in open_ports for port in common_ports):
        return f"Router might have a web interface on ports {open_ports}. Check for default credentials."
    return "No web interface detected on common ports."

# Main function to run all checks
def check_wifi_security():
    """
    Checks the security status of the Wi-Fi network.

    Returns:
        A dictionary containing the following information:
        - "Encryption": The type of encryption used by the Wi-Fi network.
        - "Router IP": The IP address of the router.
        - "Open Ports": A list of open ports on the router.
        - "SSID Hidden": Indicates whether the SSID is hidden or not.
        - "Default Password Check": Indicates whether the router is using a default password or not.
    """
    encryption = check_wifi_encryption()
    router_ip = get_router_ip()
    open_ports = scan_router_ports(router_ip)
    ssid_hidden = check_ssid_hidden()
    default_password_check = check_default_passwords(router_ip)

    return {
        "Encryption": encryption,
        "Router IP": router_ip,
        "Open Ports": open_ports,
        "SSID Hidden": ssid_hidden,
        "Default Password Check": default_password_check
    }
    


def get_wifi_password_macos(ssid):
    """
    Retrieves the Wi-Fi password for a given SSID on macOS.

    Args:
        ssid (str): The SSID of the Wi-Fi network.

    Returns:
        str: The Wi-Fi password for the specified SSID, if found in the keychain.
             If the password is not found, a message indicating the failure reason is returned.

    Raises:
        subprocess.CalledProcessError: If an error occurs while executing the command.

    """
    try:
        command = f"security find-generic-password -D 'AirPort network password' -a {ssid} -w"
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        password = result.decode('utf-8').strip()
        return password
    except subprocess.CalledProcessError as e:
        error_output = e.output.decode('utf-8').strip()
        if "could not be found in the keychain" in error_output:
            return f"Could not find the Wi-Fi password for SSID '{ssid}' in the keychain."
        elif "User interaction is not allowed" in error_output:
            return "User interaction is not allowed. Try running the script in a user session with the correct permissions."
        else:
            return f"An error occurred: {error_output}"



def get_wifi_password_windows(ssid):
    """
    Retrieves the Wi-Fi password for a given SSID on Windows.

    Args:
        ssid (str): The SSID of the Wi-Fi network.

    Returns:
        str: The Wi-Fi password if found, or an error message if the password could not be retrieved.
    """
    try:
        command = f"netsh wlan show profile name=\"{ssid}\" key=clear"
        result = subprocess.check_output(command, shell=True)
        result = result.decode('utf-8').split('\n')
        for line in result:
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                return password
        return "No password found or could not retrieve the Wi-Fi password."
    except subprocess.CalledProcessError:
        return "Could not retrieve the Wi-Fi password."


def get_wifi_password_linux(ssid):
    """
    Retrieves the Wi-Fi password for a given SSID on a Linux system.

    Args:
        ssid (str): The SSID of the Wi-Fi network.

    Returns:
        str: The Wi-Fi password if it is successfully retrieved, or a message indicating failure.

    """
    try:
        command = f"nmcli -s -g 802-11-wireless-security.psk connection show \"{ssid}\""
        result = subprocess.check_output(command, shell=True)
        password = result.decode('utf-8').strip()
        return password
    except subprocess.CalledProcessError:
        return "Could not retrieve the Wi-Fi password."
    
def get_wifi_password(ssid):
    """
    Retrieves the password for the specified Wi-Fi network.

    Args:
        ssid (str): The SSID (network name) of the Wi-Fi network.

    Returns:
        str: The password for the specified Wi-Fi network.

    Raises:
        None

    """
    os_type = platform.system()

    if os_type == "Linux":
        return get_wifi_password_linux(ssid)
    elif os_type == "Darwin":  # macOS
        return get_wifi_password_macos(ssid)
    elif os_type == "Windows":
        return get_wifi_password_windows(ssid)
    else:
        return "Unsupported operating system."

# Run the Wi-Fi security check
if __name__ == "__main__":
    security_report = check_wifi_security()
    for key, value in security_report.items():
        print(f"{key}: {value}")
