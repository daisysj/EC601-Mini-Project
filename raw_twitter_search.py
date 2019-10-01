#!/usr/bin/python
# -*- coding: utf-8 -*-
import tweepy
import json

consumer_key = '...'
consumer_secret = '...'
access_key = '...'
access_secret = '...'

def get_raw_tweets(typein):

    score = 0
    mag = 0
    typein_str = ""
    typein_list = typein.split()

    for i in typein_list:
        typein_str = typein_str + "%20" + i

    auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    results = api.search(q=typein_str, count=500, lang = "en", iso_language_code = "en")

    return results