import psutil
import time
import datetime

# Function to format bytes into a human-readable format
def format_bytes(size):
    # 2**10 = 1024
    power = 1024
    n = 0
    power_labels = {0: '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return f"{size:.2f} {power_labels[n]}B"

# Function to log network activity
def log_network_activity(interval=1):
    with open("network_activity_log.txt", "a") as log_file:
        log_file.write(f"Logging started at {datetime.datetime.now()}\n\n")
        
        while True:
            # Get network I/O statistics since boot
            net_io = psutil.net_io_counters()

            # Log the current network statistics
            log_file.write(f"Time: {datetime.datetime.now()}\n")
            log_file.write(f"Bytes Sent: {format_bytes(net_io.bytes_sent)}\n")
            log_file.write(f"Bytes Received: {format_bytes(net_io.bytes_recv)}\n")
            log_file.write(f"Packets Sent: {net_io.packets_sent}\n")
            log_file.write(f"Packets Received: {net_io.packets_recv}\n")
            log_file.write("\n")
            
            # Print to console as well
            print(f"Time: {datetime.datetime.now()}")
            print(f"Bytes Sent: {format_bytes(net_io.bytes_sent)}")
            print(f"Bytes Received: {format_bytes(net_io.bytes_recv)}")
            print(f"Packets Sent: {net_io.packets_sent}")
            print(f"Packets Received: {net_io.packets_recv}")
            print("\n")

            # Wait for the specified interval before logging again
            time.sleep(interval)

# Start logging network activity
try:
    log_network_activity()
except KeyboardInterrupt:
    print("Logging stopped.")
