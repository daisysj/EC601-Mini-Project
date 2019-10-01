#!/usr/bin/python
# -*- coding: utf-8 -*-
import google_NLapi as fun
import tweepy
import csv
import json

consumer_key = '...'
consumer_secret = '...'
access_key = '...'
access_secret = '...'

def get_tweets(typein):

    score = 0
    mag = 0
    count = 0
    typein_str = ""
    typein_list = typein.split()

    for i in typein_list:
        typein_str = typein_str + "%20" + i

    auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    results = api.search(q=typein_str, count=500, lang = "en", iso_language_code = "en")

    for j in results:
        print(j.user.screen_name, " : ", j.text, "\n")
        sentis = fun.analyze_sentiment(j.text)
        score = score + sentis[0]
        mag = mag + sentis[1]
        count = count + 1

    score = score / count
    mag = mag / count

    print("The average sentiment score is: ", score, "\n")
    print("The average sentiment magnitude is: ", mag, "\n")

    if (score <= -0.5):
        print("The sentiment is quite negative")
    elif ((score > -0.5) & (score < 0)):
        print("The sentiment is relatively negative")
    elif ((score < 0.5) & (score >= 0)):
        print("The sentiment is relatively positive")
    elif (score >= 0.5):
        print("The sentiment is quite positive")

if __name__ == '__main__':
    get_tweets(input("Enter your twitter search keyword: "))