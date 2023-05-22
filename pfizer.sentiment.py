import tweepy

consumer_key = 'oYOe9RFvv1s6Z8TyfpzXM4R5a'
consumer_secret = '78SDg96GwxZu0jOQo6vmebQi2t7Xqu75J3HsVtxIxtarIKgS2L'
access_token = '165197655-KwonLmnWxgQPiXR6Cq9ZMAscBMCTcny2E9cCkrmN'
access_token_secret = 'D4UbrKFoQkr6CJwqGLWr2Dt1eKigfiHGhIPSoS8OBx0fz'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


search_query = 'Pfizer vaccine'
num_tweets = 1000


tweets = api.search_tweets(q=search_query, tweet_mode='extended', count=num_tweets)

for tweet in tweets:
    # Process or store each tweet as desired
    print(tweet.full_text)
