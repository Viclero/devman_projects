import datetime
from urllib.parse import urlparse
now = datetime.datetime.now()

then = datetime.datetime(2023, 1, 29, 13, 15, 30)

d = now-then

t = datetime.timedelta(hours=2, minutes=30)
print(now)
print(then)
h = int(d/datetime.timedelta(hours=1))
m = int(d/datetime.timedelta(minutes=1) - h*60)

# print( f'{h}ч {m}мин' )

stay = now-then


pars = urlparse('http://bit.ly/3jrgELV')
print(
    'https://api-ssl.bitly.com/v4/bitlinks/{0}{1}/clicks/summary'.format(pars.netloc, pars.path))
