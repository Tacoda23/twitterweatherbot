import token
import requests
from tkinter import *
import math
import tweepy
import time

#twitter dev credentials

api_key = ""
api_secret = ""
bearer_token = r""
access_token = ""
access_token_secret = ""

#VisualCrossing Credentials

city = "" # name of city
state = "" # name of state
API_key = "" # Visual Crossing Weather API Key
unitGroup = "" # Units for measurement (us, metric, uk, base)

def get_observation(API_key, city, state, unitGroup):
    
    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}%20{state}/tomorrow?unitGroup={unitGroup}&include=hours&key={API_key}&contentType=json'

    #print(url)

    response = requests.get(url).json()
    
   # Tomorrow's weather conditions
    global date 
    date = response['days'][0]['datetimeEpoch']
    
    global high 
    high = response['days'][0]['tempmax']
    high = round(high) #Round to nearest number

    global FLhigh 
    FLhigh = response['days'][0]['feelslikemax']
    FLhigh = round(FLhigh) #Round to nearest number

    global low 
    low = response['days'][0]['tempmin']
    low = round(low) #Round to nearest number

    global FLlow 
    FLlow = response['days'][0]['feelslikemin']
    FLlow = round(FLlow) #Round to nearest number

    global description 
    description = response['days'][0]['description']

    global icon1
    icon1 = response['days'][0]['icon']

    global wind
    wind = response['days'][0]['windspeed']
    wind = round(wind) #Round to nearest number

    global uv
    uv = response['days'][0]['uvindex']
    uv = round(uv) #Round to nearest number

    global gust
    gust = response['days'][0]['windgust']
    gust = round(gust) #Round to nearest number

    global humidity
    humidity = response['days'][0]['humidity']
    humidity = round(humidity) #Round to nearest number

    global sunriseEpoch
    sunriseEpoch = response['days'][0]['sunriseEpoch']

    global sunsetEpoch
    sunsetEpoch = response['days'][0]['sunsetEpoch']
    



get_observation(API_key, city, state, unitGroup)

date2 = time.strftime('%m/%d', time.localtime(date))

sunset = time.strftime('%H:%M', time.localtime(sunsetEpoch))

sunrise = time.strftime('%H:%M', time.localtime(sunriseEpoch))

#emojis conversion

if (icon1 == 'clear-day'): #clear day
    icon2 = "☀️"
elif (icon1 == 'clear-night'): #clear night
    icon2 = '🌑'
elif (icon1 == 'partly-cloudy-day'): #scattered clouds day
    icon2 = '⛅'
elif (icon1 == 'partly-cloudy-night'): #scattered clouds night
    icon2 = '☁️'
elif (icon1 == 'cloudy'): #cloudy
    icon2 = '☁️'
elif (icon1 == 'wind'): #windy
    icon2 = '🌬️'
elif (icon1 == 'fog'): #foggy
    icon2 = '🌫️'
elif (icon1 == 'rain'): #rain
    icon2 = '🌧️'
elif (icon1 == 'snow'): #snow
    icon2 = '❄️'


body = f"""
Tomorrow's Weather Outlook {date2}: {icon2} {description} High of {high}°F({FLhigh}°F) and a low of {low}°F({FLlow}°F). Winds at {wind}MPH({gust}), {humidity}% humidity, and a UV of {uv}. 
🌇 {sunrise} 🌃 {sunset}
"""
print (body)

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

client.create_tweet(text=body) #posts the tweet