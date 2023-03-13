import requests
import json
from pprint import pprint
import pandas as pd

def get_by_name():
    name = input('(ex: jungle) input main word of book: ')
    #jungle example
    
    url = "https://www.googleapis.com/books/v1/volumes?q={}+intitle:keyes&key=AIzaSyBE-wVgVmGOvgsbLkETRPNc8yWgAiYDhnk".format(name)
    res = requests.get(url)
    json = res.json()

    for item in json['items']:
        title = [item['volumeInfo']['title']],
        authors = [item['volumeInfo']['authors']],
        description = [item['volumeInfo']['description']],
        categories = [item['volumeInfo']['categories']],
        country = [item['accessInfo']['country']],
        publisher = [item['volumeInfo']['publisher']],
    print("title: {}\n\nauthor: {}\n\ndescription: {}\n\ncategories: {}\n\ncountry: {}\n\npublisher: {}".format(title, authors, description, categories, country, publisher))

get_by_name()