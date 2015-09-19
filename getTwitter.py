from twython import Twython
APP_KEY = 'UYG5sjOS1NVp05INMZT1Yz3q2'
APP_SECRET = '6Sj5DlQgZTK4X88rtM4GN1qnl9wEbLHqAU8Jp3IutDd6dMJeLY'
OAUTH_TOKEN = '301518115-hbqHTK25fwdhRQRq87d69NMp7zaFVBLk5sB9zmVh'
OAUTH_TOKEN_SECRET = 'RwQrzZN8aHnq6Y24aUHaJmM8fOoq1M0XgWMqY0E31HbEV'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

try:
    user_timeline = twitter.get_user_timeline(screen_name='pythoncentral')
except TwythonError as e:
    print e

for tweet in user_timeline:
    print(tweet['text'])
