import requests
import json

# Replace with your cloud application endpoint URL
url = "https://your-cloud-application-endpoint.com/api/data"

# Example data to send to the server
data = {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "message": "Hello, this is a test message!"
}

# Headers for the request, typically specifying content-type as JSON
headers = {
    "Content-Type": "application/json"
}

# Function to send data to the cloud application endpoint
def send_data(url, data):
    try:
        # Send POST request
        response = requests.post(url, data=json.dumps(data), headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            print("Data successfully sent to the server.")
            print("Server response:", response.json())
        else:
            print(f"Failed to send data. Status code: {response.status_code}")
            print("Server response:", response.text)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Call the function to send data
send_data(url, data)
