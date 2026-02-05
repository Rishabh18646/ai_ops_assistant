import os
import requests

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def weather_tool(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"

    res = requests.get(url)
    
    if res.status_code != 200:
        return {"error": "Weather API failed", "status": res.status_code}
    
    data = res.json()

    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["description"]
    }
