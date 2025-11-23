import requests
import json
import os

CACHE_DIR = "cache"
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

def get_weather(city, api_key):
    cache_file = f"{CACHE_DIR}/{city.lower()}_weather.json"

    # Check cache first
    if os.path.exists(cache_file):
        with open(cache_file, "r") as f:
            return json.load(f)

    # API call
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if "main" not in data:
            raise ValueError("City invalid or API limit exceeded")
        # Save cache
        with open(cache_file, "w") as f:
            json.dump(data, f)
        return data
    except Exception as e:
        raise ConnectionError(f"Weather API error: {e}")
