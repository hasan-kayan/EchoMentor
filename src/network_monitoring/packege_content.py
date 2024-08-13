from scapy.all import sniff, Raw
import datetime

# Function to log packet details
def packet_callback(packet):
    # Only log if the packet has a Raw layer (which contains the payload)
    if packet.haslayer(Raw):
        # Open log file
        with open("packet_log.txt", "a") as log_file:
            # Log timestamp and packet summary
            log_file.write(f"Time: {datetime.datetime.now()}\n")
            log_file.write(f"Packet: {packet.summary()}\n")
            log_file.write(f"Raw Content: {packet[Raw].load}\n")
            log_file.write("\n")
        
        # Print to console (optional)
        print(f"Time: {datetime.datetime.now()}")
        print(f"Packet: {packet.summary()}")
        print(f"Raw Content: {packet[Raw].load}")
        print("\n")

# Function to start sniffing
def start_sniffing(interface=None):
    print(f"Starting packet sniffing on interface: {interface}")
    sniff(iface=interface, prn=packet_callback, store=0)

# Run the sniffing function
try:
    # Replace 'eth0' with your network interface (use 'None' to sniff on all interfaces)
    start_sniffing(interface=None)
except KeyboardInterrupt:
    print("Packet sniffing stopped.")
