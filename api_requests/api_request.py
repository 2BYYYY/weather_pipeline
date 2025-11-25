"""
    https://docs.apilayer.com/weatherstack/docs/quickstart-guide?utm_source=DocumentationPage&utm_medium=Referral
"""
from dotenv import load_dotenv
import os
import requests
import argparse
import json

def fetch_data():
    try:
        params = {
            "access_key": API_KEY,
            "query": COUNTRY
        }
        # Sample url: http://api.weatherstack.com/current?access_key=YOUR_ACCESS_KEY&query=COUNTRY
        response = requests.get(WEATHER_URL, params=params)
        json_response = response.json()
        foramtted_response = json.dumps(json_response, indent=2)
        return foramtted_response
    except Exception as e:
        print(f"Error in fetching the data: {e}")
        raise

def mock_data():
    data = {
            "request": {
                "type": "City",
                "query": "New York, United States of America",
                "language": "en",
                "unit": "m"
            },
            "location": {
                "name": "New York",
                "country": "United States of America",
                "region": "New York",
                "lat": "40.714",
                "lon": "-74.006",
                "timezone_id": "America/New_York",
                "localtime": "2025-11-25 00:52",
                "localtime_epoch": 1764031920,
                "utc_offset": "-5.0"
            },
            "current": {
                "observation_time": "05:52 AM",
                "temperature": 7,
                "weather_code": 116,
                "weather_icons": [
                "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png"
                ],
                "weather_descriptions": [
                "Partly cloudy"
                ],
                "astro": {
                "sunrise": "06:55 AM",
                "sunset": "04:31 PM",
                "moonrise": "11:27 AM",
                "moonset": "09:02 PM",
                "moon_phase": "Waxing Crescent",
                "moon_illumination": 19
                },
                "air_quality": {
                "co": "384.85",
                "no2": "57.05",
                "o3": "0",
                "so2": "11.05",
                "pm2_5": "19.15",
                "pm10": "19.45",
                "us-epa-index": "2",
                "gb-defra-index": "2"
                },
                "wind_speed": 7,
                "wind_degree": 219,
                "wind_dir": "SW",
                "pressure": 1025,
                "precip": 0,
                "humidity": 60,
                "cloudcover": 75,
                "feelslike": 5,
                "uv_index": 0,
                "visibility": 16,
                "is_day": "no"
            }
            }
    return data

if __name__ == "__main__":
    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument("country", nargs="+", help="Input the country or city name")
    args = parser.parse_args()

    # build the URL
    COUNTRY = " ".join(args.country)
    API_KEY = os.getenv("WEATHER_API")
    WEATHER_URL = "http://api.weatherstack.com/current"
    print(fetch_data())
