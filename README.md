# 📝 Description
This repository contains code to run a bot written in Python3, utilizing the OpenWeatherMap and VisualCrossing APIs to gather information on current weather conditions, day and nighttime forecasts, and National Weather Service (NWS) alerts. The bot pulls this information and posts it to Twitter using the Tweepy library.

Once the bot is run, it will access the OpenWeatherMap API and retrieve information such as temperature, wind speed, and humidity. This data is then processed and combined with information from the VisualCrossing API, which provides day and nighttime forecasts, as well as any NWS alerts in the area.

The bot then uses the Tweepy library to post this information to Twitter, including a brief summary of the current weather conditions and any important alerts from the NWS. The posts are made using a designated Twitter account and can be viewed by the public in real-time.

This bot is a useful tool for providing up-to-date weather information to a large audience in an easy-to-read format. It is also a great way to keep track of any weather warnings and stay safe during severe weather events.

This is a example of the bot

<a href = "https://twitter.com/OUWEATHERBOT"> <img src="https://img.shields.io/twitter/url?label=OUWEATHERBOT&style=social&url=https%3A%2F%2Ftwitter.com%2FOUWEATHERBOT"/> </a>


# 🖥️ Set-Up 

You will need aceess to Twitter's API, the basic plan should work just fine.

You will also need to create free accounts with OpenWeatherMaps and VisualCrossing


# 🐤 How to use

Install the reqiurements
```
python3 -m pip install -r requirements.txt
```
Enter your dev information and API Keys in the '' as marked
```
api_key = ""
api_secret = ""
bearer_token = r""
access_token = ""
access_token_secret = ""
```
Youll need to enter your city's name and latitude and longitude in the marked '' 
```
#OpenWeatherMap
lat = "" # latitude of city
lon = "" # longitude of city
API_key = "" # OpenWeatherMap API Key
units = "" # Units for measurement

#VisualCrossing
city = "" # name of city
state = "" # name of state
API_key = "" # Visual Crossing Weather API Key
unitGroup = "" # Units for measurement (us, metric, uk, base)
```
You can also change the body on each script to your liking, and the emojis it uses. 

```
#tweet body
tweet = f'Current weather observation: {icon2}  {description} and {temp}°F, feels like {feels_like}°F. {wind_speed}MPH winds from the {directions[degrees]} with {humidity}% humidity.'
```
