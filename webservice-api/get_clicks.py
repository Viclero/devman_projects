import os
from dotenv import load_dotenv
import requests
from urllib.parse import urlparse


def shorten_link(token, url):
    try:
        response = requests.get(url)
    except:
        print('Wrong URL!')
        return None

    headers = {
        'Authorization': token
    }
    json_values = {
        "long_url": url
    }
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(url, headers=headers, json=json_values)
    response.raise_for_status()
    bitlink = response.json()['id']
    return bitlink


def count_clicks(token, link):
    headers = {
        'Authorization': token
    }
    params = {
        "unit": 'day',
        "units": '-1'
    }
    parsed_link = urlparse(link)
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{0}{1}/clicks/summary'.format(
        parsed_link.netloc, parsed_link.path)
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    total_clicks = response.json()['total_clicks']
    return total_clicks


def is_bitlink(token, url):

    parsed_url = urlparse(url)
    headers = {
        'Authorization': token
    }
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{0}{1}'.format(
        parsed_url.netloc, parsed_url.path)
    response = requests.get(url, headers=headers)

    return response.ok


def main():
    load_dotenv()

    token = os.getenv("BITLY_TOKEN")
    user_url = input()

    if is_bitlink(token, user_url):
        count = count_clicks(token, user_url)
        print(count)
        return

    bitlink = shorten_link(token, user_url)
    print(bitlink)


if __name__ == '__main__':
    main()
