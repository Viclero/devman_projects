import requests

def show_forcast():
    cities = ['Лондон', 'аэропорт Шереметьево', 'Череповец']
    setings = {'m':'', 'n':'', 'q':'', 'T':'',  'lang': 'ru'}
    for city in cities:
      url = f'https://wttr.in/{city}' 
      response = requests.get(url, params=setings)
      response.raise_for_status()
      print(response.text)