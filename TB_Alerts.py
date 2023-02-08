import token
import requests
from tkinter import *
import math
import tweepy
import pyshorteners

#twitter dev credentials
api_key = "an3IW5VUN5LnMwtpqsUgIajSD"
api_secret = "YSsxJDGSLsuBiutZblujui9phylFB0uHGmf4z8AIVZADzPHkHJ"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAALymkQEAAAAAwaUX%2BVpmfpNGgiSZryl8CFls80E%3DSmH9T8UEv99SYfYC2UxBvQCz2E4NotRpcmOLmXVKcGtxkM7YKQ"
access_token = "1439677069126942722-7gpQDt0wNi1xbeCf5IPyrGMMLB3qky"
access_token_secret = "49pTtNHcoHn6yzYwPcvEd5YjAYlToM0CvzP9TzdCDx4r1"

city = "Norman" # name of city
state = "Oklahoma" # name of state
API_key = "5D63GEFAQUADD9WR7XHY6QK59" # Visual Crossing Weather API Key
unitGroup = "us" # Units for measurement (us, metric, uk, base)

def get_observation(API_key, city, state, unitGroup):
    
    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}%20{state}?unitGroup={unitGroup}&key={API_key}&contentType=json'

    print(url)

    response = requests.get(url).json()
    
   # weather alert
    
    event1 = response['alerts'][0]['event'] #pulls title
    global eventupper1 
    eventupper1 = (event1.upper()) #caps event

    global headline1
    headline1 = response['alerts'][0]['headline'] #pulls description

    global link1
    link1 = response['alerts'][0]['link'] #pulls link

    type_tiny = pyshorteners.Shortener() #shortens link
    global shortlink1
    shortlink1 = type_tiny.tinyurl.short(link1)
    

get_observation(API_key, city, state, unitGroup)



#print (eventupper1)
#print (headline1)
#print (shortlink1)

alert_body = f"""
{eventupper1}: {headline1}.
Read more: {shortlink1}
"""


#print (alert_body)

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

substring = 'http'

if substring in link1: #unnessary but helps prevent false posts
    client.create_tweet(text=alert_body) #posts the tweet
else:
    print('No Alerts')



