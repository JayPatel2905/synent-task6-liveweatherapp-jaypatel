import requests

API_KEY = "YOUR_API_KEY"

city_name = input("Enter city name: ")

api_url = (
    f"https://api.openweathermap.org/data/2.5/weather?"
    f"q={city_name}&appid={API_KEY}&units=metric"
)

response = requests.get(api_url)

weather_data = response.json()

print(weather_data)