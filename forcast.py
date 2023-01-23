import requests
import urllib

def show_forcast():
    city_list = ['Лондон', 'аэропорт Шереметьево', 'Череповец']
    #city_name = city.lower()
    setings = {'?M':'', 'n':'', 'q':'', 'T':'', 'u':'', 'lang': 'ru'}
    params = urllib.parse.urlencode(setings, safe='?&')
    for city_name in city_list:
      url = f'https://wttr.in/{city_name}{params}'
      print(url)
      response = requests.get(url)
      if not response.ok: 
        print('ошибка')
      response.raise_for_status()
      print(response.text)
