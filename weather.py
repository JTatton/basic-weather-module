from __future__ import print_function
import requests
import time

# READ IN API KEY FROM TEXT FILE
apikeyFile = open('apikey.txt','r')
APIKEY = apikeyFile.read()

# MAKE REQUEST
url = 'http://api.openweathermap.org/data/2.5/forecast?id=2078025&APPID=' + APIKEY
response = requests.get(url)

# Get JSON Data
jsonData = response.json()

#print(jsonData)

weatherData = jsonData['list']



