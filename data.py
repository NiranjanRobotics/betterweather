import requests
import json
import geopy
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Better Weather")


def readCity():
    file = open("info.txt", "r")
    city = file.read()
    file.close()
    return city

def describeWeather(windSpeed, pressure, precip, cloudCover, temp, humidity):
    windy = False#
    rainy = 0#
    snowy = 0#
    stormy = False#
    cloudy = 0#
    foggy = False#
    weathers = [windy, rainy, snowy, stormy, cloudy, foggy]
    forecast = []

    if windSpeed > 24: windy = True
    if precip < 0.1: rainy = 0
    elif precip < 0.5 and temp > 0: rainy = 1
    elif precip < 0.5 and not(temp > 0): snowy = 1
    elif precip < 4 and (temp > 0): rainy = 2
    elif precip < 4 and not(temp > 0): snowy = 2
    elif precip < 8 and (temp > 0): rainy = 3
    elif precip < 8 and not(temp > 0): snowy = 3
    else:
        if (pressure < 29) and (cloudCover > 70) and not(temp > 0): stormy = True
        elif not(temp > 0): rainy = 3
        else: snowy = 3
    if cloudCover < 20: cloudy = 0
    elif cloudCover < 50: cloudy = 1
    elif cloudCover < 70: cloudy = 2
    else: cloudy = 3
    if (humidity > 95) and (pressure > 31) and (windSpeed < 10) and (cloudCover > 70): foggy = True

    for weatherType in weathers:
        if weatherType == True:
            forecast.append(weatherType)
        elif weatherType == 1:
            forecast.append("slightly " + weatherType)
        elif weatherType == 2:
            forecast.append(weatherType)
        elif weatherType == 3:
            forecast.append("heavily " + weatherType)
    return forecast

def getAntipode(city):
    location = geolocator.geocode(city)
    latO, lonO = location.latitude(), location.longitude()
    latA = latO * -1
    lonA = lonO + 180
    return latA, lonA

lat, lon = getAntipode(readCity())
data = requests.get(f"http://api.weatherstack.com/current? access_key = d0a2334b8769a13ce02f5eef1b7c418e& query = {lat,lon}")
data = json.dumps(data, set_keys=True, indent=4)
forecast = describeWeather(data[2][5], data[2][8], data[2][9], data[2][11], data[2][1], data[2][10])
"""Order: windSpeed, pressure, precip, cloudCover, temp, humidity
5 windSpeed
8 pressure
9 precipitation
10 humidity
11 cloud cover
1 feels like"""

import openai

openai.api_key = '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'

prompt_weather = ""
for weather in forecast: prompt_weather += (weather + ", ")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"Write a pickup line for a {prompt_weather} day relating to that weather.",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

file = open("info.txt", "w")
file.write(response)
file.close()