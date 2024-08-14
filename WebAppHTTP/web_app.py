from flask import Flask, request, jsonify

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    # Get the user's IP address
    user_ip = request.remote_addr
    
    # Log the IP address
    print(f"IP Address: {user_ip}")
    
    # Simple HTML page to fetch location
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Location Fetcher</title>
        <script>
            function getLocation() {
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(showPosition, showError);
                } else {
                    document.getElementById("location").innerHTML = "Geolocation is not supported by this browser.";
                }
            }

            function showPosition(position) {
                const locationData = {
                    latitude: position.coords.latitude,
                    longitude: position.coords.longitude,
                    accuracy: position.coords.accuracy
                };

                fetch('/location', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(locationData)
                })
                .then(response => response.json())
                .then(data => {
                    document.getElementById("location").innerHTML = "Location logged successfully.";
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
            }

            function showError(error) {
                switch(error.code) {
                    case error.PERMISSION_DENIED:
                        document.getElementById("location").innerHTML = "User denied the request for Geolocation.";
                        break;
                    case error.POSITION_UNAVAILABLE:
                        document.getElementById("location").innerHTML = "Location information is unavailable.";
                        break;
                    case error.TIMEOUT:
                        document.getElementById("location").innerHTML = "The request to get user location timed out.";
                        break;
                    case error.UNKNOWN_ERROR:
                        document.getElementById("location").innerHTML = "An unknown error occurred.";
                        break;
                }
            }
        </script>
    </head>
    <body onload="getLocation()">
        <h1>Location Fetcher</h1>
        <p id="location">Fetching location...</p>
    </body>
    </html>
    """
    return html_content

# Route to handle the location data
@app.route('/location', methods=['POST'])
def log_location():
    location_data = request.json
    print(f"Location Data: {location_data}")
    
    return jsonify({'status': 'success', 'message': 'Location logged successfully'})

if __name__ == '__main__':
    app.run(debug=True)
