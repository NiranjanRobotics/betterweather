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


def getAntipode(city):
    location = geolocator.geocode(city)
    latO, lonO = location.latitude(), location.longitude()
    latA = latO * -1
    lonA = lonO + 180
    return latA, lonA


# thing:
rain = ["Do you want to dance in the rain with me? I promise I'll keep you warm.", "I don't mind getting wet, as long as I'm standing next to you in the rain."]
sun = ["Are you the sun? Because you are so beautiful it is blinding!", "The sun must be jealous of how hot you are."]
cloud = ["The future seems cloudy, but I can see one with us."]
snow = ["You are as unique as a snowflake."]
hail = ["Will you HAIL me as your king/queen?"]
wind = ["My hat just got blown away, but will you stay with me?"]
foggy = [""]

lat, lon = getAntipode(readCity())
data = requests.get(f"http://api.weatherstack.com/current? access_key = d0a2334b8769a13ce02f5eef1b7c418e& query = {lat,lon}")
data = json.dumps(data, set_keys=True, indent=4)
#5 windSpeed
#8 pressure
#9 precipitation
#10 humidity
#11 cloud cover
#12 feels like
def describeWeather(windSpeed, pressure, precip, cloudCover, feelslike, humidity):
    windy = False
    rainy = 0#
    snowy = 0#
    stormy = False#
    humid = False#
    cloudy = 0#
    foggy = False
    temp = 2

    if windSpeed > 24: windy = True
    if precip < 0.1: rainy = 0
    elif precip < 0.5 and feelslike > 0: rainy = 1
    elif precip < 0.5 and not(feelslike > 0): snowy = 1
    elif precip < 4 and (feelslike > 0): rainy = 2
    elif precip < 4 and not(feelslike > 0): snowy = 2
    elif precip < 8 and (feelslike > 0): rainy = 3
    elif precip < 8 and not(feelslike > 0): snowy = 3
    else:
        if (pressure < 29) and (cloudCover > 70) and not(feelslike > 0): stormy = True
        else: rainy = 3
    if cloudCover < 20: cloudy = 0
    elif cloudCover < 50: cloudy = 1
    elif cloudCover < 70: cloudy = 2
    else: cloudy = 3
    if (humidity > 95) and (pressure > 31) and (windSpeed < 10) and (cloudCover > 70): foggy = True

    