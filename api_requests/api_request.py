"""
    https://docs.apilayer.com/weatherstack/docs/quickstart-guide?utm_source=DocumentationPage&utm_medium=Referral
"""
from dotenv import load_dotenv
import os
import requests
import argparse

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("country", nargs="+", help="Input the country or city name")
args = parser.parse_args()

# build the URL
COUNTRY = " ".join(args.country)
API_KEY = os.getenv("WEATHER_API")
WEATHER_URL = "http://api.weatherstack.com/current"

def fetch_data():
    try:
        params = {
            "access_key": API_KEY,
            "query": COUNTRY
        }
        # Sample url: http://api.weatherstack.com/current?access_key=YOUR_ACCESS_KEY&query=New York
        response = requests.get(WEATHER_URL, params=params)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    print(fetch_data())
