import webbrowser
import platform

# URL to open
url = "https://web.whatsapp.com/"

# Open the default browser
def open_browser():
    try:
        # For Mac
        if platform.system() == "Darwin":
            webbrowser.get('safari').open(url)
        # For Windows
        elif platform.system() == "Windows":
            webbrowser.get('windows-default').open(url)
        else:
            # Fallback to default browser
            webbrowser.open(url)
    except webbrowser.Error:
        print("Failed to open the browser. Please try manually.")

# Run the function
open_browser()
