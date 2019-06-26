import tweepy
from textblob import TextBlob

consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"

access_token = "YOUR_ACCESS_TOKEN"
access_secret = "YOUR_ACCESS_SECRET"


#Authenticating to Twitter
auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

#Word we want to Analysis in Twitter

tweets = api.search('ANYTHING_YOU_WANT_TO_ANALYSE')

#Print the tweets and Sentiment Analysis
for tweet in tweets:
    print(tweet.txt)
    analysis = TextBlob(tweet.txt)
    print(analysis.sentiment)
