import token
import requests
from tkinter import *
import math
import tweepy
import pyshorteners

#twitter dev credentials
api_key = ""
api_secret = ""
bearer_token = r""
access_token = ""
access_token_secret = ""

#location information
city = "" # name of city
state = "" # name of state
API_key = "" # Visual Crossing Weather API Key
unitGroup = "" # Units for measurement (us, metric, uk, base)

def get_observation(API_key, city, state, unitGroup):
    
    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}%20{state}?unitGroup={unitGroup}&key={API_key}&contentType=json'

    #print(url)

    response = requests.get(url).json()
    
   # pull weather alert
    
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

#unnessary but helps prevent false posts, will get "index out of range" if no alerts
if substring in link1: 
    client.create_tweet(text=alert_body) #posts the tweet
else:
    print('No Alerts')



