# Method -> GET/POST/PATCH/PUT/DELETE  OPTIONS/HEAD
# URL/URI    https://api.cern.ch?name=Kevin&location=Geneva
# Headers -> Content: application/json
from http.client import responses

# Status Code
# Body -> info
# Headers

import requests
import json

def fetch_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "hourly": "temperature_2m,relativehumidity_2m",
        "timezone": "auto"
    }

    response = requests.get(url, params=params)
    # if posting JSON data use the request.post(url, params=params, json=<>)
    response.raise_for_status()

    return response.json()

try:
    data = fetch_weather(51, 0)
    current = data.get("current_weather")
    temp = current.get("temperature")
    print(f"Current temperature: {temp}")
    with open("weather_london.json", "w") as file:
        json.dump(data, file, indent=2)
    print("Weather data saved.")
except Exception as error:
    print(f"Error: {error}")














