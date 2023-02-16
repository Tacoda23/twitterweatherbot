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

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

#Check if already tweeted

userlookup = client.get_user(username='OUWEATHERBOT')

userid = (userlookup.data.id)

tweets = client.get_users_tweets(id=userid, tweet_fields=['text'])

test = str(tweets)


def get_observation(API_key, city, state, unitGroup):
    
    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}%20{state}?unitGroup={unitGroup}&key={API_key}&contentType=json'

    #print(url)

    response = requests.get(url).json()
    
   # pull weather alert
    
    alerts = response['alerts']

    
    try:
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

        global alert_body
        alert_body = f"""
{eventupper1}: {headline1}. 
Read more: {shortlink1}
        """
            
        print (alert_body)
        #print (test)
        #print (headline1)

        if headline1 in test:
            print ('already tweeted')
        else:
            print ('just tweeted')
            client.create_tweet(text=alert_body)
            

       

    except:
        event1 = "No current weather alerts"
        print (event1)

    
   
get_observation(API_key, city, state, unitGroup)



