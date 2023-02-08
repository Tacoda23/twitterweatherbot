import token
import requests
from tkinter import *
import math
import tweepy

#twitter dev credentials
api_key = "an3IW5VUN5LnMwtpqsUgIajSD"
api_secret = "YSsxJDGSLsuBiutZblujui9phylFB0uHGmf4z8AIVZADzPHkHJ"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAALymkQEAAAAAwaUX%2BVpmfpNGgiSZryl8CFls80E%3DSmH9T8UEv99SYfYC2UxBvQCz2E4NotRpcmOLmXVKcGtxkM7YKQ"
access_token = "1439677069126942722-7gpQDt0wNi1xbeCf5IPyrGMMLB3qky"
access_token_secret = "49pTtNHcoHn6yzYwPcvEd5YjAYlToM0CvzP9TzdCDx4r1"

lat = "35.205894" # latitude of city
lon = "-97.445717" # longitude of city
API_key = "afef94b7d142c4e338316adc68986937" # OpenWeatherMap API Key
units = "imperial" # Units for measurement

def get_observation(API_key, lat, lon, units):
    
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units={units}"

    #print(url) #can display test url

    response = requests.get(url).json()
    
    global description #current weather condition
    description = response['weather'][0]['description']

    global icon #weather icon
    icon = response['weather'][0]['icon']
    
    global icon2 #emoji placeholder
    icon2 = ''
    
    global temp #temperature
    temp = response['main']['temp']
    temp = round(temp) #Round temperature nearest number

    global feels_like #feels like temperature
    feels_like = response['main']['feels_like']
    feels_like = round(feels_like) #Round to nearest number

    global humidity #current humidity
    humidity= response['main']['humidity']
    humidity = round(humidity) #Round to nearest number
    
    global wind_speed #wind speed
    wind_speed= response['wind']['speed']
    wind_speed = round(wind_speed) #Round to nearest number

    global directions #wind direction
    global degrees
    deg= response['wind']['deg']
    degrees = deg # coverts degrees into direction
    directions = ['North', 'Northeast', 'East', 'Southeast', 'South', 'Southwest', 'West', 'Northwest'];
    degrees = degrees * 8 / 360;
    degrees = round(degrees)
    degrees = (degrees + 8) % 8


get_observation(API_key, lat, lon, units)

#converts weather icon code to an emoji
if (icon == '01d'): #clear dat
    icon2 = "☀️"
elif (icon == '01n'): #clear night
    icon2 = '🌑'
elif (icon == '02d'): #scattered clouds day
    icon2 = '⛅'
elif (icon == '02n'): #scattered clouds night
    icon2 = '☁️'
elif (icon == '03d'): #cloudy day
    icon2 = '☁️'
elif (icon == '03n'): #cloudy night
    icon2 = '☁️'
elif (icon == '04d'): #broken clouds day
    icon2 = '🌥️'
elif (icon == '04n'): #broken clouds night
    icon2 = '☁️'
elif (icon == '09d'): #shower rain day
    icon2 = '🌦️'
elif (icon == '09n'): #shower rain night
    icon2 = '🌧️'
elif (icon == '10d'): #rain day
    icon2 = '🌧️'
elif (icon == '10n'): #rain night
    icon2 = '🌧️'
elif (icon == '11d'): #thunderstorm day
    icon = '🌩️'
elif (icon == '11n'): #thunderstorm night
    icon = '🌩️'
elif (icon == '13d'): #snow day
    icon2 = '❄️'
elif (icon == '13n'): #snow night
    icon2 = '❄️'
elif (icon == '50d'): #mist day
    icon2 = '☁️'
elif (icon == '50n'): #mist night
    icon2 = '☁️'



#tweet body
tweet = f'Current weather observation: {icon2}  {description} and {temp}°F, feels like {feels_like}°F. {wind_speed}MPH winds from the {directions[degrees]} with {humidity}% humidity.'

print (tweet)

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

API.update_status(text=tweet) #posts the tweet