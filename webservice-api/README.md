## Description

Program shows how many clicks a bitly link has. If entered URL doesn't have short link, program return it.

## Installation

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
 
 To get token sign up [bit.ly](https://bit.ly) . Go Profile->API->Access token

 
## To Start counting

run get_clicks.py

Enter bit.ly short link or URL
