import psutil
import datetime

def format_bytes(size):
    """
    Convert bytes to a human-readable format.

    Parameters:
    - size (int): The size in bytes to be converted.

    Returns:
    - str: The human-readable format of the size.

    Example:
    >>> format_bytes(1024)
    '1.00 KB'
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
            - time (datetime): The current timestamp.
            - bytes_sent (str): The number of bytes sent.
            - bytes_received (str): The number of bytes received.
            - packets_sent (int): The number of packets sent.
            - packets_received (int): The number of packets received.
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
