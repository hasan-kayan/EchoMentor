import platform
import subprocess

def get_recent_processes():
    os_type = platform.system()

    if os_type == "Windows":
        return get_recent_processes_windows()
    elif os_type == "Darwin":
        return get_recent_processes_mac()
    else:
        return "Unsupported Operating System"

def get_recent_processes_windows():
    try:
        cmd = 'powershell "Get-Process | Sort-Object StartTime -Descending | Select-Object Name, StartTime -First 10"'
        result = subprocess.check_output(cmd, shell=True)
        return result.decode('utf-8')
    except Exception as e:
        return f"Error: {e}"

def get_recent_processes_mac():
    try:
        # Command to get recent processes and sort by time
        cmd = "ps -eo comm,lstart | tail -n +2 | sort -k5M -k6 -k7 | tail -n 10"
        result = subprocess.check_output(cmd, shell=True)
        return result.decode('utf-8')
    except Exception as e:
        return f"Error: {e}"

# Execute the function and print the result
print(get_recent_processes())
