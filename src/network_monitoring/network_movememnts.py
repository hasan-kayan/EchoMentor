# network_monitor.py

import psutil
import datetime

def format_bytes(size):
    """
    Convert bytes to a human-readable format.
    """
    power = 1024
    n = 0
    power_labels = {0: '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return f"{size:.2f} {power_labels[n]}B"

def get_network_activity():
    """
    Get the current network activity.
    
    Returns:
        dict: A dictionary containing the network activity statistics.
    """
    # Get network I/O statistics since boot
    net_io = psutil.net_io_counters()

    # Prepare the network statistics data
    network_data = {
        "time": datetime.datetime.now(),
        "bytes_sent": format_bytes(net_io.bytes_sent),
        "bytes_received": format_bytes(net_io.bytes_recv),
        "packets_sent": net_io.packets_sent,
        "packets_received": net_io.packets_recv,
    }

    return network_data
