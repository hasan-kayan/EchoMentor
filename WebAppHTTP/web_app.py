from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    # Get the user's IP address
    user_ip = request.remote_addr
    
    # Log the IP address
    print(f"IP Address: {user_ip}")
    
    # Get location info using an external API
    try:
        response = requests.get(f'http://ip-api.com/json/{user_ip}')
        location_data = response.json()
    except Exception as e:
        location_data = {'error': 'Unable to get location data'}
    
    # Return a simple response
    return jsonify({
        'message': 'Welcome to the web app!',
        'ip_address': user_ip,
        'location': location_data
    })

if __name__ == '__main__':
    app.run(debug=True)
