from twython import Twython

def getTweets(apiKey, apiSecret, oauthToken, oauthTokenSecret, screenName, numberOfTweets)
	twitter = Twython(apiKey, apiSecret, oauthToken, oauthTokenSecret)

	try:
	    user_timeline = twitter.get_user_timeline(screen_name=screenName,
	    	count=numberOfTweets, include_rts="1")
	except TwythonError as e:
	    print e

	tweetsList = [tweet['text'] for tweet in user_timeline]
	return tweetsList
	    


def main():
    #TEST
    API_KEY = keys.TWITTER_API_KEY
	API_SECRET = keys.TWITTER_API_SECRET
	OAUTH_TOKEN = keys.TWITTER_OAUTH_TOKEN
	OAUTH_TOKEN_SECRET = keys.TWITTER_OAUTH_TOKEN_SECRET
	screenName = 'AToregozhina'
	numberOfTweets = 200
    tweetsList = getTweets(API_KEY, API_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET, screenName, numberOfTweets)
    print tweetsList 

if __name__ == "__main__":
    main()