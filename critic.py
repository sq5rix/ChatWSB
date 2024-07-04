import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_URL = os.getenv('API_URL')

def get_critique(prompt):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'  # Remove this line if no API key is required
    }
    
    data = {
        'text': prompt
    }
    
    response = requests.post(API_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json().get('critique', 'No critique found')
    else:
        return f"Error: {response.status_code}, {response.text}"

if __name__ == "__main__":
    prompt = input("Enter the text to critique: ")
    critique = get_critique(prompt)
    print("Critique:")
    print(critique)