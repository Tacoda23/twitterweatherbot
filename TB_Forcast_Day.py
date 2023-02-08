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

city = "norman" # name of city
state = "Oklahoma" # name of state
API_key = "5D63GEFAQUADD9WR7XHY6QK59" # Visual Crossing Weather API Key
unitGroup = "us" # Units for measurement (us, metric, uk, base)

def get_observation(API_key, city, state, unitGroup):
    
    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}%20{state}?unitGroup={unitGroup}&include=hours%2Cfcst&key={API_key}&contentType=json'

    #print(url)

    response = requests.get(url).json()
    
   # 8:00 CT weather conditions
    global temp1 
    temp1 = response['days'][0]['hours'][17]['temp']
    temp1 = round(temp1) #Round temperature nearest number
    
    global condition1 
    condition1 = response['days'][0]['hours'][8]['conditions']

    global icon1
    icon1 = response['days'][0]['hours'][8]['icon']

    #print (temp1)
    #print (condition1)

    # 11:00 CT weather conditions
    global temp2 
    temp2 = response['days'][0]['hours'][11]['temp']
    temp2 = round(temp2) #Round temperature nearest number
    
    global condition2 
    condition2 = response['days'][0]['hours'][11]['conditions']

    global icon3
    icon3 = response['days'][0]['hours'][11]['icon']
    
    #print (temp2)
    #print (condition2)

    # 13:00 CT weather conditions
    global temp3 
    temp3 = response['days'][0]['hours'][13]['temp']
    temp3 = round(temp3) #Round temperature nearest number
    
    global condition3
    condition3 = response['days'][0]['hours'][13]['conditions']

    global icon5
    icon5 = response['days'][0]['hours'][13]['icon']

    #print (temp3)
    #print (condition3)

    # 15:00 CT weather conditions
    global temp4 
    temp4 = response['days'][0]['hours'][15]['temp']
    temp4 = round(temp3) #Round temperature nearest number
    
    global condition4
    condition4 = response['days'][0]['hours'][15]['conditions']

    global icon7
    icon7 = response['days'][0]['hours'][15]['icon']

    #print (temp3)
    #print (condition3)



get_observation(API_key, city, state, unitGroup)

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

if (icon3 == 'clear-day'): #clear day
    icon4 = "☀️"
elif (icon3 == 'clear-night'): #clear night
    icon4 = '🌑'
elif (icon3 == 'partly-cloudy-day'): #scattered clouds day
    icon4 = '⛅'
elif (icon3 == 'partly-cloudy-night'): #scattered clouds night
    icon4 = '☁️'
elif (icon3 == 'cloudy'): #cloudy
    icon4 = '☁️'
elif (icon3 == 'wind'): #windy
    icon4 = '🌬️'
elif (icon3 == 'fog'): #foggy
    icon4 = '🌫️'
elif (icon3 == 'rain'): #rain
    icon4 = '🌧️'
elif (icon3 == 'snow'): #snow
    icon4 = '❄️'

if (icon5 == 'clear-day'): #clear day
    icon6 = "☀️"
elif (icon5 == 'clear-night'): #clear night
    icon6 = '🌑'
elif (icon5 == 'partly-cloudy-day'): #scattered clouds day
    icon6 = '⛅'
elif (icon5 == 'partly-cloudy-night'): #scattered clouds night
    icon6 = '☁️'
elif (icon5 == 'cloudy'): #cloudy
    icon6 = '☁️'
elif (icon5 == 'wind'): #windy
    icon6 = '🌬️'
elif (icon5 == 'fog'): #foggy
    icon6 = '🌫️'
elif (icon5 == 'rain'): #rain
    icon6 = '🌧️'
elif (icon5 == 'snow'): #snow
    icon6 = '❄️'

if (icon7 == 'clear-day'): #clear day
    icon68 = "☀️"
elif (icon7 == 'clear-night'): #clear night
    icon8 = '🌑'
elif (icon7 == 'partly-cloudy-day'): #scattered clouds day
    icon8 = '⛅'
elif (icon7 == 'partly-cloudy-night'): #scattered clouds night
    icon8 = '☁️'
elif (icon7 == 'cloudy'): #cloudy
    icon8 = '☁️'
elif (icon7 == 'wind'): #windy
    icon8 = '🌬️'
elif (icon7 == 'fog'): #foggy
    icon8 = '🌫️'
elif (icon7 == 'rain'): #rain
    icon8 = '🌧️'
elif (icon7 == 'snow'): #snow
    icon8 = '❄️'

body = f"""
Weather forcast for the rest of today:
Now      {icon2}  {condition1} and {temp1}°F
7:00p    {icon4}  {condition2} and {temp2}°F
10:00p   {icon6}  {condition3} and {temp3}°F
11:00p   {icon8}  {condition4} and {temp4}°F
"""
#print (body)

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

#client.create_tweet(text=body) #posts the tweet