import os
import tweepy
import json
import sys
import geocoder
from decouple import config

# API Keys and Tokens
api_key = config('API_KEY')
api_key_secret = config('API_SECRET_KEY')
access_token = config('ACCESS_TOKEN')
access_token_secret = config('ACCESS_TOKEN_SECRET')

# Authorization and Authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

if __name__ == "__main__":
    # Available Locations
    available_loc = api.trends_available()

    # writing a JSON file that has the available trends around the world
    with open("available_locs_for_trend.json","w") as wp:
        wp.write(json.dumps(available_loc, indent=1))

    # Trends for Specific Country
    loc = sys.argv[1]     # location as argument variable
    geo = geocoder.osm(loc) # getting object that has location's latitude and longitude

    closest_loc = api.trends_closest(geo.lat, geo.lng)
    trends = api.trends_place(closest_loc[0]['woeid'])
    #parsed = json.loads(trends)
    print(trends)
    #print(type(trends))
    #print(json.dumps(parsed, indent=4))

    # writing a JSON file that has the latest trends for that location
    with open("twitter_{}_trend.json".format(loc),"w") as wp:
        wp.write(json.dumps(trends, indent=1))

    # print("######### Last 20 RGV Tweets ############")
    # name = "RGVzoomin"
    # tweetcount = 20
    # results = api.user_timeline(id=name, count=tweetcount)
    # for tweet in results:
    #     print(tweet.text)
    # print("#########################################")
