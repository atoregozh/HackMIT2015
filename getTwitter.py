from twython import Twython
API_KEY = 'QLnA03i5k8js1WzUDaIqGFDOr'
API_SECRET = 'F5JvaONVQnHYeohwEUQ5i8n99x2HCrE7xl5G2ai3oQ6YNO9Tc4'
OAUTH_TOKEN = '301518115-86uulgB7tNxnSDcsJVvRlRWKN3nn3V3ftm5EDi0t'
OAUTH_TOKEN_SECRET = '6efj5xyl8uhdk2g0V8jp1iwdqVUHeDeoxhMDXDSL2DV0e'

twitter = Twython(API_KEY, API_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

try:
    user_timeline = twitter.get_user_timeline(screen_name='AToregozhina',
    	count="200", include_rts="1")
except TwythonError as e:
    print e

for tweet in user_timeline:
    print(tweet['text'])
