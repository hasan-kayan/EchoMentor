from file_finder.file_finder import * 
from image_finder.media_finder import *
from network_monitoring.network_movememnts import *
from network_monitoring.packege_content import *
from port_scanner.port_scanner import *
from program_usage.program_usage import *
from recent_process.recent_process import *
from wifi_sec.wifi_sec import *


class computer_scanner:
    def __init__(self):
        self.root_folder = os.path.expanduser("~")
        self.output_file = "found_files.txt"
        self.media_folder = "Media_Files"
        self.network_interface = None
        self.port_range = (1, 1024)
        self.program_name = None
        self.wifi_interface = None

    def search_files(self, extension):
        search_files(self.root_folder, extension, self.output_file)
    def search_media(self):
        media_files = search_media_files(self.root_folder)
        clone_media_files(media_files, self.media_folder)
    def scan_network(self):
        start_sniffing(self.network_interface)
    def scan_ports(self):
        open_ports = scan_ports(*self.port_range)
        if open_ports:
            print(f"Available ports: {open_ports}")
        else:
            print("No available ports found.")
