#Twitter Sentiment Analysis

import tweepy
from textblob import TextBlob

consumer_key = 'ArdXLxDwcRIT1NZoRzfp1B2FT'
consumer_secret = 'dhe5SaWIrqhnoOn6dyWiYMElOH75n3ISeOenvzBgEZh4RR1DcQ'
access_token = '386157913-Fuy6MxHBHlMCuJyQaQ5z8EVJCbImD1hs1IlG8KO1'
access_token_secret = 'HItfC9VQE4CATVlqR36KWJVkMhhgGYcMwXqUW5IDQpiHh'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
print("Please Enter the Word you would like to perform a sentiment analysis on!")
User_Input = input()


#Retrieve Tweets
public_tweets = api.search(User_Input)

# CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
# and label each one as either 'positive' or 'negative', depending on the sentiment
# You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)

    # Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")