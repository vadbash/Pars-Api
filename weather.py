import requests
import json
from pprint import pprint
import pandas as pd

def weather():
    city = input("Input a city to see the weather: ")
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=cb1657161a4c396d7510303571ee489f".format(city)

    res = requests.get(url)
    json = res.json()
    df = pd.DataFrame({
        'city': json['name'],
        'country': (json['sys']['country']),
        'temp': (json['main']['temp']),
        'min temp': (json['main']['temp_min']),
        'max temp': (json['main']['temp_max']),
        'humidity': (json['main']['humidity']),
        'pressure': (json['main']['pressure']),
        'wind': (json['wind']['speed']),
        'visibility': [json['visibility']]
    })
    return df
   
pprint(weather())