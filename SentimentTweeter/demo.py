from textblob import TextBlob
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Narendra Modi',)

for tweet in public_tweets:
  f = open('t','a')
  f.writelines(tweet.text.encode('utf-8'))
  f.write('\n')
  f.write('\n')
  f.close()
