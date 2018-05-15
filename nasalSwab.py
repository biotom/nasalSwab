# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 23:24:59 2018

@author: Tom
"""

import os
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener 
#pulled from environmental variables for security. DO NOT PUT KEYS DIRECTLY IN CODE.
twitter_access_secret = os.environ['twitter_access_secret']
twitter_access_token = os.environ['twitter_access_token']
twitter_consumer_key = os.environ['twitter_consumer_key']
twitter_consumer_secret = os.environ['twitter_consumer_secret'] 

#OAuth  authentication handler interface. 
auth = OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
auth.set_access_token(twitter_access_token, twitter_access_secret)

api = tweepy.API(auth)#tweepy API wrapper. Passed in the authentication handler

class FluListener(StreamListener):#inherits from base class StreatmListener
    def on_error(self,status):
        print(status)
    def on_data(self,data):
        with open('flu_tweets.json', 'a') as f: #opens file in append mode
            f.write(data)


if __name__ == '__main__':
    flu_listener = FluListener()
    sneeze = Stream(auth, flu_listener)
    sneeze.filter(track=['flu','influenza'], follow=['16616061', '146569971', '855482932173168640']) #follow CDCFlu, CDCGov, BARDA