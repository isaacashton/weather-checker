import json
import os
import requests
import sys

# get api key
appid = os.environ.get('WEATHER_API_KEY')
# make the api call
response = requests.get('http://api.openweathermap.org/data/2.5/weather?q' +
                        '=Bowser,ca&appid=' + appid)

# error checking
if response.status_code != 200:
    print('An error occured: ' + str(response.status_code))
    input('> ')
    sys.exit()

# deserialize the json
weather = response.json()

weather_main = weather ['weather'][0]['main']
weather_description = weather['weather'][0]['description']
weather_current_temp = round(weather['main']['temp'] - 273.15, 1)
weather_min_temp = round(weather['main']['temp_min'] - 273.15, 1)
weather_max_temp = round(weather['main']['temp_max'] - 273.15, 1)
weather_humidity = weather['main']['humidity']

print('Today\'s weather: ' + weather_main + ', '
        + weather_description + ' with highs of ' + str(weather_max_temp)
        + ' and lows of ' + str(weather_min_temp))
print('Current temperature: ' + str(weather_current_temp))
print('Current humidity: ' + str(weather_humidity))
input()
