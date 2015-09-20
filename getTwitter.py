from twython import Twython
API_KEY = keys.TWITTER_API_KEY
API_SECRET = keys.TWITTER_API_SECRET
OAUTH_TOKEN = keys.TWITTER_OAUTH_TOKEN
OAUTH_TOKEN_SECRET = keys.TWITTER_OAUTH_TOKEN_SECRET

twitter = Twython(API_KEY, API_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

try:
    user_timeline = twitter.get_user_timeline(screen_name='AToregozhina',
    	count="200", include_rts="1")
except TwythonError as e:
    print e

for tweet in user_timeline:
    print(tweet['text'])
