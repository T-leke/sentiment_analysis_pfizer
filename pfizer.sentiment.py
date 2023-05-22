import tweepy
import psycopg2
import os
import datetime

key = os.environ.get('consumer_key')
secret = os.environ.get('consumer_secret')
token = os.environ.get('access_token')
token_secret = os.environ.get('access_token_secret')


auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(token, token_secret)

api = tweepy.API(auth)


search_query = 'Pfizer vaccine'
num_tweets = 1000


tweets = api.search_tweets(q=search_query, tweet_mode='extended', count=num_tweets)

conn = psycopg2.connect(
host="localhost",
port="5432",
database="Bookscrape",
user="postgres",
password="#Tolexy5038"
)

cur = conn.cursor()

for tweet in tweets:
    # Process or store each tweet as desired
    tweet_text = tweet.full_text
    tweet_time = tweet.created_at

    tweet_time = datetime.datetime.strftime(tweet_time, '%Y-%m-%d %H:%M:%S+00:00')

    #pushing the tweets to the database

    tweet_text = tweet_text.replace("'", "''")
    # create_table_query = """
    # CREATE TABLE pfizer (
    # timestamp TIMESTAMP,
    # Tweets TEXT
    # )
    # """

    # cur.execute(create_table_query)

    insert = "INSERT INTO pfizer (timestamp, Tweets) VALUES ('{}', E'{}')".format(tweet_time, tweet_text)

    cur.execute(insert)
    
conn.commit()
cur.close()