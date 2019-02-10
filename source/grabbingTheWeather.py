#!/usr/bin/env python
# coding: utf-8

# In[26]:


#Grabbing the Weather Project for Dwolla Internship
#By: Vy Ngo


# In[49]:


#module allows http requests
import requests 

def weatherGrab():
    #user inputs desired city
    city = input('Where are you? ')

    #Open weather map api call w/ key and specified city and units
    weather_API = ('http://api.openweathermap.org/data/2.5/weather?appid=3529ca8740c75206b4c62134c4344442&q=' + city +'&units=imperial')

    #accepts data from request in json format
    data = requests.get(weather_API).json()

    #specifies data location in json format
    weather_data = data['main']['temp']

    #outputs temperature in imperial units
    print(city + ' Weather: \n' + str(weather_data))
    
weatherGrab()


# 
