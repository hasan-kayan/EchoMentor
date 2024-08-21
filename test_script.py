from lib import (
    search_files,
    search_media_files, collect_and_clone_media_files,
    format_bytes, get_network_activity,
    get_packet_details, packet_callback, start_sniffing,
    get_network_interfaces, get_connected_devices, get_dns_servers, get_dhcp_leases, get_router_ip, get_detailed_network_info,
    monitor_signal_strength, monitor_bandwidth_usage, analyze_channel_interference, suggest_optimal_channel,
    get_image_metadata,
    scan_ports, main,
    get_last_used_apps, log_last_used_apps,
    get_recent_processes, get_recent_processes_windows, get_recent_processes_mac,
    scan_open_ports, check_upnp_vulnerability, check_nat_pmp_vulnerability, check_common_exploits,
    check_wpa3_support, check_wifi_encryption, detect_weak_encryption, save_security_protocol_history, get_security_protocol_history
)

# Add simple test cases for each function
print(get_detailed_network_info())
print(monitor_signal_strength())
# Continue testing other functions...
