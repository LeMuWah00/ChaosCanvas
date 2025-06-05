from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_URL = "https://stablediffusionapi.com/api/v4/dreambooth"
API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/generate_art', methods=['POST'])
def generate_art():
    data = request.get_json()
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {"prompt": prompt}

    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        return jsonify({"image_url": response.json().get("image_url", "Error generating image")})
    else:
        return jsonify({"error": f"API request failed with status {response.status_code}"}), response.status_code

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
