import requests
from urllib.parse import urlparse


def shorten_link(token, url):
    headers = {
        'Authorization': token
    }
    data = {
        "long_url": url
    }
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    bitlink = response.json()['id']
    return bitlink


def count_clics(token, link):
    headers = {
        'Authorization': token
    }
    params = {
        "unit": 'day',
        "units": '-1'
    }
    pars = urlparse(link)
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{0}{1}/clicks/summary'.format(
        pars.netloc, pars.path)
    response = requests.get(url, headers=headers, params=params)
    total_clicks = response.json()['total_clicks']
    return total_clicks


def is_bitlink(url):
    pars = urlparse(url)
    return pars.netloc == 'bit.ly'


def main(token, url):
    if is_bitlink(url):
        try:
            count = count_clics(token, url)
            return count
        except requests.exceptions.HTTPError:
            print("bad bitlink for count")

    try:
        bitlink = shorten_link(token, url)
        return bitlink
    except requests.exceptions.HTTPError:
        print("bad address for short link")
