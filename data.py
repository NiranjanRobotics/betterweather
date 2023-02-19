import requests
import json
import openai
import geopy
from geopy.geocoders import Nominatim

user_city = input("City, State >>> ")
file = open("info.txt", "w")
file.write(user_city)
file.close()

#City Antipode Finder
geolocator = Nominatim(user_agent="Better Weather")


def readCity():
    file = open("info.txt", "r")
    city = file.read()
    file.close()
    return city

def describeWeather(windSpeed, pressure, precip, cloudCover, temp, humidity):
    windy = False
    rainy = 0
    snowy = 0
    stormy = False
    cloudy = 0
    foggy = False
    sunny = True
    weathers = [windy, rainy, snowy, stormy, cloudy, foggy, sunny]
    strings = ['windy', 'rainy', 'snowy', 'stormy', 'cloudy', 'foggy', 'sunny']
    forecast = []

    file = open("info.txt", "w")
    file.write(str(temp))
    file.close()

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
    if cloudy != 0: sunny = False

    for weatherType in weathers:
        if weatherType == True:
            forecast.append(strings[weathers.index(weatherType)])
        elif weatherType == 1:
            forecast.append("slightly " + strings[weathers.index(weatherType)])
        elif weatherType == 2:
            forecast.append(strings[weathers.index(weatherType)])
        elif weatherType == 3:
            forecast.append("heavily " + strings[weathers.index(weatherType)])
    return forecast

def getAntipode(city):
    location = geolocator.geocode(city)
    latO = str(location.latitude)
    lonO = str(location.longitude)
    latO, lonO = eval(latO), eval(lonO)
    latA = latO * -1
    lonA = lonO + 180
    return latA, lonA

#Weather of Antipode
lat, lon = getAntipode(readCity())
key = "90724d418f86432b979195649231902"
print(f"http://api.weatherapi.com/v1/current.json?key={key}&q={lat},{lon}")
data = requests.get(f"http://api.weatherapi.com/v1/current.json?key={key}&q={lat},{lon}")
data = json.dumps(data.json(), sort_keys=True, indent=4)
data = json.loads(data)
forecast = describeWeather(
    int(data['current']['wind_mph']),
    int(data['current']['pressure_in']),
    int(data['current']['precip_mm']), 
    int(data['current']['cloud']), 
    int(data['current']['temp_f']), 
    int(data['current']['humidity'])
)

"""Order: windSpeed, pressure, precip, cloudCover, temp, humidity
5 windSpeed
8 pressure
9 precipitation
10 humidity
11 cloud cover
1 feels like"""

#AI pickup lines
openai.api_key = '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'

prompt_weather = ""
for weather in forecast: prompt_weather += (weather + " ")

file = open("info.txt", "a")
file.write("\nToday is a " + prompt_weather + " day!")
file.close()

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"Write a hot pickup line for a {prompt_weather} day relating to that weather.",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

file = open("info.txt", "a")
file.write(response['choices'][0]['text'])
file.close()