import requests

API_KEY = "PASTE_YOUR_OPENWEATHERMAP_API_KEY_HERE"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        if response.status_code == 404:
            print("City not found. Please check the city name.")
            return
        if response.status_code == 401:
            print("Invalid API key. Add your OpenWeatherMap API key to the code.")
            return

        response.raise_for_status()
        data = response.json()

        temperature_c = data["main"]["temp"]
        temperature_f = (temperature_c * 9 / 5) + 32
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"].title()
        wind_speed = data["wind"]["speed"]

        print("\n" + "=" * 40)
        print(f"Weather for {data['name']}")
        print("=" * 40)
        print(f"Temperature: {temperature_c:.1f} °C / {temperature_f:.1f} °F")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition}")
        print(f"Wind speed: {wind_speed} m/s")

    except requests.exceptions.Timeout:
        print("Request timed out. Please try again.")
    except requests.exceptions.ConnectionError:
        print("Network error. Check your internet connection.")
    except requests.exceptions.RequestException as error:
        print(f"Weather service error: {error}")

print("=" * 40)
print("        BASIC WEATHER APP")
print("=" * 40)

while True:
    city = input("\nEnter a city name (or type 'exit'): ").strip()

    if city.lower() == "exit":
        print("Goodbye!")
        break

    if not city:
        print("City name cannot be empty.")
        continue

    if API_KEY == "PASTE_YOUR_OPENWEATHERMAP_API_KEY_HERE":
        print("\nFirst add your OpenWeatherMap API key at the top of this file.")
        print("Then run the program again.")
        continue

    get_weather(city)
