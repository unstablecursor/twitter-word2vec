import tweepy
import json
from tweepy import OAuthHandler


# Accessing Twitter API
consumer_key = "f7VxaS2wZdVKMUUVQCpIE0Ib0" # API key
consumer_secret = "278JKjPW4CekJbBd5JXU6CZ03TjdWWddCRk8vT57Cwe5JLASix" # API secret
access_token = "607485944-lqFmgbQfNfhUpyGZYe2j0ZCy2BHqQXRjfm8LIwrG"
access_secret = "amdqIZLeD4xfsdRrLacVSNJonLkQcnHQkuyZUbd1jFdBp"



auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def getTweets():
    tweets = []
    data = tweepy.Cursor(api.search, q= "#EVET", languages = 'tr').items(1000)
    for tweet in data:
        tweets.append(tweet._json)
    return tweets


target = open('result.txt', 'w')
for x in getTweets():
    target.write(x['text'].encode('utf-8'))
