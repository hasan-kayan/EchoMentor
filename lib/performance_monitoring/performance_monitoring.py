import platform
import subprocess
import time
import psutil

def monitor_signal_strength():
    """
    Monitors and returns the Wi-Fi signal strength (RSSI) of the current connection.

    Returns:
        str: The current signal strength in dBm.
    """
    os_type = platform.system()

    if os_type == "Linux" or os_type == "Darwin":  # Linux and macOS
        try:
            result = subprocess.check_output(["iwconfig"])
            result = result.decode("utf-8")
            for line in result.splitlines():
                if "Signal level" in line:
                    signal_strength = line.split("Signal level=")[-1].split(" ")[0]
                    return f"Signal strength: {signal_strength} dBm"
        except Exception as e:
            return f"Error monitoring signal strength on {os_type}: {str(e)}"

    elif os_type == "Windows":
        try:
            result = subprocess.check_output(["netsh", "wlan", "show", "interfaces"])
            result = result.decode('utf-8')
            for line in result.splitlines():
                if "Signal" in line:
                    signal_strength = line.split(":")[1].strip()
                    return f"Signal strength: {signal_strength}%"
        except Exception as e:
            return f"Error monitoring signal strength on Windows: {str(e)}"

    return "Unsupported operating system."

def monitor_bandwidth_usage(duration=10):
    """
    Monitors and returns the bandwidth usage (upload and download speeds) over a specified duration.

    Args:
        duration (int, optional): The duration to monitor bandwidth usage, in seconds. Defaults to 10 seconds.

    Returns:
        dict: A dictionary containing upload and download speeds in bytes per second.
    """
    start_data = psutil.net_io_counters()
    time.sleep(duration)
    end_data = psutil.net_io_counters()

    download_speed = (end_data.bytes_recv - start_data.bytes_recv) / duration
    upload_speed = (end_data.bytes_sent - start_data.bytes_sent) / duration

    return {
        "Download Speed": f"{download_speed:.2f} B/s",
        "Upload Speed": f"{upload_speed:.2f} B/s"
    }

def analyze_channel_interference():
    """
    Analyzes and returns Wi-Fi channel interference from nearby networks.

    Returns:
        dict: A dictionary containing the channels in use and recommendations for the optimal channel.
    """
    os_type = platform.system()

    channels_in_use = []
    if os_type == "Linux" or os_type == "Darwin":  # Linux and macOS
        try:
            result = subprocess.check_output(["iwlist", "scanning"])
            result = result.decode("utf-8")
            for line in result.splitlines():
                if "Channel:" in line:
                    channel = line.split(":")[1].strip()
                    channels_in_use.append(channel)
        except Exception as e:
            return f"Error analyzing channel interference on {os_type}: {str(e)}"

    elif os_type == "Windows":
        try:
            result = subprocess.check_output(["netsh", "wlan", "show", "networks", "mode=bssid"])
            result = result.decode('utf-8')
            for line in result.splitlines():
                if "Channel" in line:
                    channel = line.split(":")[1].strip()
                    channels_in_use.append(channel)
        except Exception as e:
            return f"Error analyzing channel interference on Windows: {str(e)}"

    optimal_channel = suggest_optimal_channel(channels_in_use)
    return {
        "Channels In Use": channels_in_use,
        "Optimal Channel Suggestion": optimal_channel
    }

def suggest_optimal_channel(channels_in_use):
    """
    Suggests the optimal Wi-Fi channel based on channels in use.

    Args:
        channels_in_use (list): A list of channels currently in use.

    Returns:
        int: The suggested optimal Wi-Fi channel.
    """
    all_channels = set(range(1, 12))  # Common Wi-Fi channels
    used_channels = set(int(channel) for channel in channels_in_use)
    available_channels = all_channels - used_channels

    if available_channels:
        return min(available_channels)  # Suggest the lowest unused channel
    return min(used_channels)  # Fallback to the lowest used channel if all are in use
