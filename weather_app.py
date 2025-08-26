import os
import requests
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("API_KEY")


BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
UNITS = "metric"
DEFAULT_CITY = "istanbul"


def get_input():
    city = input("Enter the city name you wanna see the weather: ")
    whatsee = input("Enter what you wanna see (weather, temperature, wind, sea level): ").lower()
    return city, whatsee

def fetch_weather(city):
    url = f"{BASE_URL}?q={city}&appid={api_key}&units={UNITS}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data
    else:
        return False

def get_weather(city, whatsee, data):
    if not data:
        print("data not found")
        return False
    elif whatsee == "weather":
        print(f"In {city} The weather is: {data['weather'][0]['description']}")
    elif whatsee == "temperature":
        print(f"In {city} The temperature is: {data['main']['temp']} C")
    elif whatsee == "wind":
        print(f"In {city} The wind is {data['wind']}")
    elif whatsee == "sea level":
        if "sea_level" in data['main']:
            print(f"In {city} The sea level is {data['main']['sea_level']}")
        else:
            print("There is no sea level in this city")
    else:
        print("Invalid input")
        print("Try again")
        return False

    return True

def api_test():
    testurl = f"{BASE_URL}?q={DEFAULT_CITY}&appid={api_key}&units={UNITS}"
    testresponse = requests.get(testurl)
    data1 = testresponse.json()
    if testresponse.status_code == 200:
        print("api clearly works")
    else:
        print("api error")
        print(int(testresponse.status_code))

def main():
    choice = input("If you wanna test api first press (y) if you dont press something else:")
    if choice.lower() == "y":
        api_test()
        input("Press any key to continue...")
    while True:
        city, whatsee = get_input()
        data = fetch_weather(city)
        if not fetch_weather(city):
            print("City is not found, Please try again")
            continue
        success = get_weather(city, whatsee, data)
        if not success :
            print("Please enter a valid Weather parameter (weather, temperature, wind, sea level) ")
            continue
        again = input("Do you wanna search something again y/n:")
        if again != "y":
            print("Goodbye")
            break

main()