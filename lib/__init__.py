from file_finder import search_files
from .image_finder import search_media_files, collect_and_clone_media_files
from .network_monitoring import (
    format_bytes, get_network_activity,
    get_packet_details, packet_callback, start_sniffing,
    get_network_interfaces,
    get_connected_devices,
    get_dns_servers,
    get_dhcp_leases,
    get_router_ip,
    get_detailed_network_info
    
)

from .performance_monitoring import (
      monitor_signal_strength,
    monitor_bandwidth_usage,
    analyze_channel_interference,
    suggest_optimal_channel
)
from .photo_analizer import get_image_metadata
from .port_scanner import scan_ports, main
from .program_usage import  get_last_used_apps, log_last_used_apps
from .recent_process import get_recent_processes, get_recent_processes_windows, get_recent_processes_mac 
from .vulnerability_scanning import (
    scan_open_ports,
    check_upnp_vulnerability,
    check_nat_pmp_vulnerability,
    check_common_exploits
)
from .wifi_sec import  (
    check_wpa3_support,
    check_wifi_encryption,
    detect_weak_encryption,
    save_security_protocol_history,
    get_security_protocol_history
)






