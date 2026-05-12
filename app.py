import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

print("\n======= LIVE WEATHER APPLICATION =======")

city_name = input("Enter city name: ")

api_url = (
    f"https://api.openweathermap.org/data/2.5/weather?"
    f"q={city_name}&appid={API_KEY}&units=metric"
)

response = requests.get(api_url)

weather_data = response.json()

if weather_data["cod"] == 200:

    temperature = weather_data["main"]["temp"]

    humidity = weather_data["main"]["humidity"]

    weather_description = (
        weather_data["weather"][0]["description"]
    )

    wind_speed = weather_data["wind"]["speed"]

    print("\n======= WEATHER REPORT =======")
    print(f"City: {city_name}")
    print(f"Temperature: {temperature} °C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather_description}")
    print(f"Wind Speed: {wind_speed} m/s")

else:
    print("\nCity not found.")