from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("HUGGINGFACE_API_KEY")
API_URL = "https://stablediffusionapi.com/api/v4/dreambooth"

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

@app.route('/', methods=['GET'])
def home():
    return "ChaosCanvasAI backend is live!", 200

@app.route('/generate_art', methods=['POST'])
def generate_art():
    data = request.get_json()
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {
        "key": API_KEY,
        "model_id": "YOUR_MODEL_ID",
        "prompt": prompt,
        "negative_prompt": "",
        "width": 512,
        "height": 512,
        "samples": 1,
        "num_inference_steps": 20
    }

    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        return jsonify({"image_url": response.json().get("image_url", "Error generating image")})
    else:
        return jsonify({"error": f"API request failed with status {response.status_code}"}), response.status_code

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
