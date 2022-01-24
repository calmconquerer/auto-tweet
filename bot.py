import tweepy
from dotenv import dotenv_values

config = dotenv_values(".env")

api_key = config.get("API_KEY")
api_secret = config.get("API_SECRET_KEY")

access_token = config.get("ACCESS_TOKEN")
access_token_secret = config.get("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = api.home_timeline()
for tweet in tweets:
    print(tweet.text)
