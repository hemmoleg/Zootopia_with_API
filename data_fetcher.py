import requests
import os
from dotenv import load_dotenv

def fetch_data(animal_name):
    headers = {
        "X-API-Key": os.getenv('API_KEY')
    }
    response = requests.get(f"https://api.api-ninjas.com/v1/animals?name={animal_name}", headers=headers)
    return response.json()

load_dotenv()
