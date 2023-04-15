import tweepy
import pandas as pd

user_key = "EnDz7gkde5lPh0uPFbJGuyAbd"
user_secret = "J1mTNw5B5OEmmxkfFfVj0kxO9raGquPkqkqpCTeGz1MnV8G3lK"
access_token = "1410964135974608899-0gQFEa2WJ6QxXw0oWDxrVAKzbl9xCQ"
access_token_secret = "wVkn5OsNQVK0LBcaGmP962o85wF3Q3GSYLv2wypsRwDhB"
# BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAABnqlAEAAAAAYcRHua9tDQPKKmzllo3tx8D8yEI % 3DJv5zcDj4M413ggBkhi0UIuilwgXE9L0MIkxcFa1sc6gpmw6lSN"

auth = tweepy.OAuthHandler(
    user_key,
    user_secret
)

auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth, wait_on_rate_limit=True)

public_tweets = api.home_timeline()

colums = ['Time', 'User', 'Tweet']
data = []


handle = 'Averek7'
user = api.get_user(screen_name=handle)

for tweet in public_tweets:

    data.append([tweet.created_at, tweet.user.screen_name, tweet.text])

df = pd.DataFrame(data, columns=colums)

df.to_csv('tweets.csv')
print(df)
