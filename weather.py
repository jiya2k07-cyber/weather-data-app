import os
from dotenv import load_dotenv
import requests
from datetime import datetime
load_dotenv()
api_key=os.getenv("API_KEY")

if api_key is None:
    print("API KEY is not found..")
    exit()
city=input("Enter city name: ")
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
try:
    response=requests.get(url,timeout=5)
    data=response.json()
    
    if data["cod"]==200:
        sunrise=datetime.fromtimestamp(data['sys']['sunrise']) #fromtimestamp will convert into date and time 
        sunset=datetime.fromtimestamp(data['sys']['sunset'])
        print("\n ----------WEATHER REPORT----------")
        print(f"\n🌍  City: {data['name']}")
        print(f"🌡️  Temperature: {data['main']['temp']}°C")
        print(f"🤒  feels like: {data['main']['feels_like']}°C")
        print(f"💧  Humidity: {data['main']['humidity']}%")
        print(f"🌥️  Weather: {data['weather'][0]['description'].title()}")
        print(f"🌬️  Wind speed: {data['wind']['speed']} m/s")
       # print(f"🌅 Sunrise: {data['sys']['sunrise']}") return unix timestamps.
       # print(f"🌇 Sunset: {data['sys']['sunset']}")
        print(f"🌅 Sunrise: {sunrise.strftime('%I:%M %p')}")
        print(f"🌇 Sunset: {sunset.strftime('%I:%M %p')}")
    else:
        print("❌ City not found!")
except requests.exceptions.Timeout:
    print("⌛ The server took too long to respond.")
except requests.exceptions.ConnectionError:
    print("❌ No Internet Connection!")