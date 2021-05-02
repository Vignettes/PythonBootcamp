### HTTP Introduction

### Our goals
# A. Describe what happens when you type a URL into URL bar
# B. Describe the request/response cycle
# C. Explain what a request or response header is, and give examples
# D. Explain the different categories of response codes
# E. Compare GET and POST requests


# When you go to google.com what happens is:
# 1. DNS lookup - finds the correct address
# 2. Computer make a REQUST to a server 
# 3. Server processes the REQUEST
# 4. Server issues a RESPONSE

# DNS lookup is like a phonebook for the web. 
# Google.com --> DNS Server --> 172.182.14.1

# HTTP Headers
# Sent with both request and response
# Provide additional information about the request or response

# Request headers
# Accept - acceptable content-types for resposnes (e.g. html, json, xml)
# Cache-control - specify caching behavior
# User-agent - contains info about software used to make request

# Response headers
# Access-control-allow-origin -specify domains that can make requests
# Allowed - HTTP verbs that are allowed in requests

# Response status codes
# 2xx -success
# 3xx - redirect
# 4xx - client error (your fault)
# 5xx - server error (not your fault)

### HTTP Verbs

# GET and POST

# GET for retrieving 
# Data passed as a query string
# Should have no "side-effects"
# Can be bookmarked

# POST for writing data
# Data passed in a request body
# Can have "side-effects"
# Can't be bookmarked


### APIs
# API - application programming interface 
# Version of a website, intended to allow computers/code to interact.


### Using the requests module

import requests # install using pip first

res = requests.get('https://www.google.com') # request to get the website
print(res) # 200 response as it was found successfully
print(res.headers) # returns the header information
print(res.text) # returns the html of the page (code of it, since this is a site)

### Requesting JSON with Python

dadjokes = requests.get('https://www.icanhazdadjoke.com/', headers={"Accept": "text/plain"}) # returns only plain text
print()
print(dadjokes.text)

dadjokes2 = requests.get('https://www.icanhazdadjoke.com/', headers={"Accept": "application/json"}) # returns only JSON
print(dadjokes2.json()) #returns the JSON response as a dictionary


### Sending requests with params
# What is a query string?
# A way to pass data to a server as part of a get
# http://www.example.com/?key1=value1&key2=value2

from random import choice

user_input = input("What do you want to search for? ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": user_input}, ).json()


num_jokes = res["total_jokes"]
results = res["results"]
if num_jokes > 1:
    print(f"There {num_jokes} jokes about {user_input}")
    print(choice(results)['joke'])
elif num_jokes == 1:
    print(f"there is 1 joke about {user_input}")
    print([results][0]['joke'])
else:
    print("there are no jokes")