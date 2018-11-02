## for New York City, New York ##

# make an api call
import requests, json
# the url is from dark sky api, however, I inserted the coordinates for New York City at the end of the URL
api_url = 'https://api.darksky.net/forecast/2de8a3b9c654d1e5a816bd7cd6038e08/40.7128,74.0060'

weather = requests.get(api_url).json()
# define the data that you are attempting to extract
currently = weather ['currently']
summary = currently ['summary']
humidity = currently ['humidity']
temperature = currently ['temperature']
# 'summary' extracts a description of the current weather (sunny, overcast, etc.), 'humidity' extracts what the current level of humidity is, and 'temperature' extracts the current temperature
print(summary, humidity, temperature)
# this will print out three parsed data points: one for 'sumary' one for 'humidity' and one for 'temperature'

## side note --> change longitude and lattitude at the end of the URL to change the place in which the weather is being recorded ##
