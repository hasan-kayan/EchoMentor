import os
import platform
import subprocess
import datetime

def get_last_used_apps_windows():
    """
    Retrieves the last used applications on Windows.

    Returns:
        str: A string with information about the last used applications.
    """
    try:
        cmd = (
            'powershell "Get-Process | Sort-Object StartTime | '
            'Select-Object Name, StartTime | Where-Object { $_.StartTime -ne $null } | '
            'Sort-Object StartTime -Descending | Select-Object -First 10"'
        )
        result = subprocess.check_output(cmd, shell=True)
        return result.decode('utf-8')
    except Exception as e:
        return f"Error: {e}"

def get_last_used_apps_mac():
    """
    Retrieves the last used applications on Mac.

    Returns:
        str: A string with information about the last used applications.
    """
    try:
        script = '''
        tell application "System Events"
            set app_list to ""
            repeat with a_process in (get processes whose background only is false)
                set app_list to app_list & name of a_process & " " & short date string of (current date) & " " & time string of (current date) & linefeed
            end repeat
        end tell
        return app_list
        '''
        result = subprocess.check_output(['osascript', '-e', script])
        return result.decode('utf-8')
    except Exception as e:
        return f"Error: {e}"

def get_last_used_apps():
    """
    Gets the last used applications based on the operating system.

    Returns:
        str: A string with information about the last used applications or an error message if the OS is unsupported.
    """
    os_type = platform.system()

    if os_type == "Windows":
        return get_last_used_apps_windows()
    elif os_type == "Darwin":
        return get_last_used_apps_mac()
    else:
        return "Unsupported Operating System"

def log_last_used_apps():
    """
    Logs the last used applications to a file.

    Returns:
        str: A string with information about the last used applications.
    """
    apps_info = get_last_used_apps()

    log_file = "last_used_apps.txt"
    with open(log_file, 'w') as f:
        f.write(f"Last Used Applications ({datetime.datetime.now()}):\n\n")
        f.write(apps_info)

    print(f"Last used applications logged to {log_file}")
    return apps_info

# Example usage:
# apps_info = get_last_used_apps()
# print(apps_info)
