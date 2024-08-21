import platform
import subprocess
import os
import json
import datetime

def check_wpa3_support():
    """
    Checks if the current Wi-Fi network supports WPA3 encryption.

    Returns:
        str: A message indicating whether WPA3 is supported or not.
    """
    os_type = platform.system()

    if os_type == "Linux":
        try:
            result = subprocess.check_output(['iw', 'dev'])
            result = result.decode('utf-8')
            if "WPA3" in result:
                return "WPA3 is supported."
            return "WPA3 is not supported."
        except Exception as e:
            return f"Error checking WPA3 support on Linux: {str(e)}"

    elif os_type == "Darwin":  # macOS
        try:
            result = subprocess.check_output(
                ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-I"]
            )
            result = result.decode('utf-8')
            if "WPA3" in result:
                return "WPA3 is supported."
            return "WPA3 is not supported."
        except Exception as e:
            return f"Error checking WPA3 support on macOS: {str(e)}"

    elif os_type == "Windows":
        try:
            result = subprocess.check_output(["netsh", "wlan", "show", "interfaces"])
            result = result.decode('utf-8')
            if "WPA3" in result:
                return "WPA3 is supported."
            return "WPA3 is not supported."
        except Exception as e:
            return f"Error checking WPA3 support on Windows: {str(e)}"

    return "Unsupported operating system."

def check_wifi_encryption():
    """
    Checks the Wi-Fi encryption type and returns the SSID and security type.

    Returns:
        str: A string containing the SSID and security type of the Wi-Fi connection.
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

def detect_weak_encryption():
    """
    Detects if the Wi-Fi network is using weak or deprecated encryption methods (e.g., WEP, WPA without TKIP/AES).

    Returns:
        str: A message indicating whether weak encryption is detected or not.
    """
    encryption_info = check_wifi_encryption()

    if "WEP" in encryption_info:
        return "Weak encryption detected: WEP is in use."
    elif "WPA" in encryption_info and not ("TKIP" in encryption_info or "AES" in encryption_info):
        return "Weak encryption detected: WPA without TKIP/AES."
    return "No weak encryption detected."

def save_security_protocol_history(security_info, history_file="security_protocol_history.json"):
    """
    Saves the current security protocol information to a history file.

    Args:
        security_info (str): The current security protocol information.
        history_file (str, optional): The file where the history is stored. Defaults to "security_protocol_history.json".

    Returns:
        None
    """
    history = []
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            history = json.load(f)

    history.append({
        "timestamp": str(datetime.datetime.now()),
        "security_info": security_info
    })

    with open(history_file, 'w') as f:
        json.dump(history, f)

def get_security_protocol_history(history_file="security_protocol_history.json"):
    """
    Retrieves the history of security protocols used by the network.

    Args:
        history_file (str, optional): The file where the history is stored. Defaults to "security_protocol_history.json".

    Returns:
        list: A list of dictionaries containing timestamped security protocol information.
    """
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            return json.load(f)
    return []
