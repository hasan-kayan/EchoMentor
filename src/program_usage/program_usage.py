import os
import platform
import subprocess
import datetime

# Function to get last used applications on Windows
def get_last_used_apps_windows():
    try:
        # Use a Windows command to get last used applications
        cmd = 'powershell "Get-Process | Sort-Object StartTime | Select-Object Name, StartTime | Where-Object { $_.StartTime -ne $null } | Sort-Object StartTime -Descending | Select-Object -First 10"'
        result = subprocess.check_output(cmd, shell=True)
        return result.decode('utf-8')
    except Exception as e:
        return f"Error: {e}"

# Function to get last used applications on Mac
def get_last_used_apps_mac():
    try:
        # Use AppleScript to get the last used applications on Mac
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

# Function to log last used applications
def log_last_used_apps():
    os_type = platform.system()

    if os_type == "Windows":
        apps_info = get_last_used_apps_windows()
    elif os_type == "Darwin":
        apps_info = get_last_used_apps_mac()
    else:
        apps_info = "Unsupported Operating System"

    # Save the result to a log file
    log_file = "last_used_apps.txt"
    with open(log_file, 'w') as f:
        f.write(f"Last Used Applications ({datetime.datetime.now()}):\n\n")
        f.write(apps_info)

    print(f"Last used applications logged to {log_file}")
    print(apps_info)

# Run the function to log last used applications
log_last_used_apps()
