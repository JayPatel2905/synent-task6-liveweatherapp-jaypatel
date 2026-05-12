import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

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

    print("\n====== WEATHER REPORT ======")
    print(f"City: {city_name}")
    print(f"Temperature: {temperature} °C")
    print(f"Humidity: {humidity}%")

else:
    print("\nCity not found.")