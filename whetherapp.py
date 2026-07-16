"""
Weather App in Python Using API
--------------------------------
Beginner Python project that fetches live weather data
using the OpenWeatherMap API.

Before running:
1. Go to https://openweathermap.org/api and create a free account.
2. Get your API key from the dashboard.
3. Replace 'YOUR_API_KEY' below with your actual key.
4. Install the requests library if not already installed:
   pip install requests
"""

import requests
# ----------------------------
# Your OpenWeatherMap API Key
# ----------------------------
API_KEY = "2956c36f34ca7b86307569d8d9b29480"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """Fetch weather data for a given city using OpenWeatherMap API."""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Celsius temperature
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            display_weather(data)
        else:
            print(f"Error: {data.get('message', 'City not found!')}")

    except requests.exceptions.RequestException as e:
        print("Network error:", e)


def display_weather(data):
    """Nicely print the weather details."""
    city = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    weather_desc = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print("\n----- WEATHER REPORT -----")
    print(f"City        : {city}, {country}")
    print(f"Temperature : {temp}°C")
    print(f"Feels Like  : {feels_like}°C")
    print(f"Condition   : {weather_desc.capitalize()}")
    print(f"Humidity    : {humidity}%")
    print(f"Wind Speed  : {wind_speed} m/s")
    print("---------------------------\n")


def main():
    print("=== Python Weather App ===")
    while True:
        city = input("Enter city name (or 'quit' to exit): ").strip()

        if city.lower() == "quit":
            print("Goodbye!")
            break

        if city == "":
            print("Please enter a valid city name.\n")
            continue

        get_weather(city)


if __name__ == "__main__":
    main()
