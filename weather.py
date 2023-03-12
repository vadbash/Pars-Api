import requests
import json
from pprint import pprint

city = input("Input a city to see the weather: ")

if city == "":
    print("please enter a city")
    exit()
else:
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=cb1657161a4c396d7510303571ee489f".format(city)

res = requests.get(url)
json = res.json()
pprint(json)