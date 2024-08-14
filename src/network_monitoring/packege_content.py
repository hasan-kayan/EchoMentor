# packet_sniffer.py

from scapy.all import sniff, Raw
import datetime

def get_packet_details(packet):
    """
    Extract and return details of a packet if it contains a Raw layer.
    
    Args:
        packet (scapy.packet.Packet): The packet to extract details from.
    
    Returns:
        dict: A dictionary containing the time, summary, and raw content of the packet.
    """
    if packet.haslayer(Raw):
        return {
            "time": datetime.datetime.now(),
            "summary": packet.summary(),
            "raw_content": packet[Raw].load
        }
    return None

def packet_callback(packet):
    """
    Callback function to be called for each captured packet.
    
    Args:
        packet (scapy.packet.Packet): The captured packet.
    
    Returns:
        dict: The packet details if available, otherwise None.
    """
    return get_packet_details(packet)

def start_sniffing(interface=None):
    """
    Start sniffing packets on a specified network interface.
    
    Args:
        interface (str): The network interface to sniff on (e.g., 'eth0'). If None, sniff on all interfaces.
    
    Returns:
        generator: A generator yielding packet details as they are captured.
    """
    print(f"Starting packet sniffing on interface: {interface}")
    return sniff(iface=interface, prn=packet_callback, store=0)
