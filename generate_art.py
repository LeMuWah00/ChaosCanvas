import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="fal-ai",
    api_key=os.environ["HF_TOKEN"],
)

# output is a PIL.Image object
image = client.text_to_image(
    "Astronaut riding a horse",
    model="stabilityai/stable-diffusion-3.5-large",
)
def generate_image(prompt):
    import requests
    
    API_URL = "https://stablediffusionapi.com/api/v4/dreambooth"  # Replace with actual API URL
    API_KEY = os.getenv("huggingface_api_key"  # Replace with your real API key
    
    data = {"prompt": prompt}
    headers = {"Authorization": f"Bearer {API_KEY}"}
    
    response = requests.post(API_URL, json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json()["image_url"]
    else:
        return "Error generating image."
