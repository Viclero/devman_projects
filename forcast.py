import requests
import urllib

def show_forcast():
    city_name = ['Лондон', 'аэропорт Шереметьево', 'Череповец']
    setings = {'M':'', 'n':'', 'q':'', 'T':'', 'u':'', 'lang': 'ru'}
    for city in city_name:
      url = 'https://wttr.in/'+city
      response = requests.get(url, params=setings)
      response.raise_for_status()
      print(response.text)