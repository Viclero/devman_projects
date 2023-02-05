## Description

Program shows how many clicks a bitly link has. If entered URL doesn't have short link, program return it.

## Requirements

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
``` 

## Environment variables
 
BITLY_TOKEN is used for [bit.ly](https://bit.ly) access.

Location for token is  .env

.env example:
```
BITLY_TOKEN = 'd8c8a967a1f2256b691986u8021d26cd1347dfec'
```
 
 To get token sign up [bitly.com](https://bitly.com) . Go Profile->API->Access token

 
## Work example

* short link
```
> get_clicks.py
https://yandex.ru       
bit.ly/3jrgELV
``` 

* URL
```
> get_clicks.py
https://bit.ly/3jrgELV 
5
```

