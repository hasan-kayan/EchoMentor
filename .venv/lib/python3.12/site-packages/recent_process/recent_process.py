import platform
import subprocess

def get_recent_processes():
    """
    Retrieves the most recent processes based on the operating system.

    Returns:
        str: A string with information about the most recent processes or an error message if the OS is unsupported.
    """
    os_type = platform.system()

    if os_type == "Windows":
        return get_recent_processes_windows()
    elif os_type == "Darwin":
        return get_recent_processes_mac()
    else:
        return "Unsupported Operating System"

def get_recent_processes_windows():
    """
    Retrieves the most recent processes on a Windows system.

    Returns:
        str: A string with information about the most recent processes.
    """
    try:
        cmd = 'powershell "Get-Process | Sort-Object StartTime -Descending | Select-Object Name, StartTime -First 10"'
        result = subprocess.check_output(cmd, shell=True)
        return result.decode('utf-8')
    except Exception as e:
        return f"Error: {e}"

def get_recent_processes_mac():
    """
    Retrieves the most recent processes on a macOS system.

    Returns:
        str: A string with information about the most recent processes.
    """
    try:
        cmd = "ps -eo comm,lstart | tail -n +2 | sort -k5M -k6 -k7 | tail -n 10"
        result = subprocess.check_output(cmd, shell=True)
        return result.decode('utf-8')
    except Exception as e:
        return f"Error: {e}"

# Example usage:
# processes_info = get_recent_processes()
# print(processes_info)
