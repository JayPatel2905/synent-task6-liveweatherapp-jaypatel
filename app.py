import requests
import os
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("API_KEY")

print("\n========= LIVE WEATHER APPLICATION =========")

while True:

    city_name = input("\nEnter city name: ")

    api_url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"q={city_name}&appid={API_KEY}&units=metric"
    )

    try:

        response = requests.get(api_url)

        weather_data = response.json()

        if weather_data["cod"] == 200:

            main_data = weather_data["main"]

            current_temperature = main_data["temp"]

            feels_like = main_data["feels_like"]

            humidity_level = main_data["humidity"]

            weather_description = (
                weather_data["weather"][0]["description"]
            )

            wind_speed = weather_data["wind"]["speed"]

            country_name = weather_data["sys"]["country"]

            print("\n=========== WEATHER REPORT ===========")
            print(f"City: {city_name}, {country_name}")
            print(f"Temperature: {current_temperature} °C")
            print(f"Feels Like: {feels_like} °C")
            print(f"Humidity: {humidity_level}%")
            print(f"Wind Speed: {wind_speed} m/s")
            print(f"Weather Condition: {weather_description}")

        else:
            print("\nCity not found. Please check spelling.")

    except requests.exceptions.ConnectionError:
        print("\n⚠ Internet connection error.")

    except Exception as error:
        print("\nSomething went wrong.")
        print(error)

    repeat_choice = input(
        "\nCheck another city? (yes/no): "
    ).lower()

    if repeat_choice != "yes":
        print("\nWeather Application Closed Successfully.")
        break