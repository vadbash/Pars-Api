import requests
import json
from pprint import pprint
import pandas as pd

def get_weather():
    city = input("Input a city to see the weather: ")
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=cb1657161a4c396d7510303571ee489f".format(city)
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame({
        'city': data['name'],
        'country': (data['sys']['country']),
        'temp': (data['main']['temp']),
        'min temp': (data['main']['temp_min']),
        'max temp': (data['main']['temp_max']),
        'humidity': (data['main']['humidity']),
        'pressure': (data['main']['pressure']),
        'wind': (data['wind']['speed']),
        'visibility': [data['visibility']]
    })
    return df

weather_data = get_weather()
pprint(weather_data)