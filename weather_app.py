import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
UNITS = "metric"
DEFAULT_CİTY = "istanbul"

def show_weather():
    city = input("Enter the city name you wanna see the weather: ")
    whatsee = input("Enter what you wanna see (weather, temperature, wind, sea level): ")

    url = f"{BASE_URL}?q={city}&appid={api_key}&units={UNITS}"
    response = requests.get(url)
    data = response.json()

    if whatsee == "weather":
        print(f"In {city} The weather is: {data['weather'][0]['description']}")

    elif whatsee == "temperature":
        print(f"In {city} The temperature is: {data['main']['temp']} C")

    elif whatsee == "wind":
        print(f"In {city} The wind is {data['wind']}")

    elif whatsee == "sea level":
        print(f"In {city} The sea level is {data['main']['sea_level']}")
    else:
        print("Invalid input")

def api_test():
    url = f"{BASE_URL}?q={DEFAULT_CİTY}&appid={api_key}&units={UNITS}"api_key
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        print("The api works clearly:)")
    else:
        print("Something went wrong!")


def whatyouwant():
    whichone = input("if you wanna test the api first Enter y / to pass and check the weather directly press something else:")
    if whichone == "y":
        api_test()
        continue1 = input("press y to continue:")
        if continue1 == "y":
            show_weather()
    else:
        show_weather()

whatyouwant()
