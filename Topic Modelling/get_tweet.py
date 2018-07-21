import tweepy
import csv

consumer_key = "9XF8SGxwqUUyEOfZp4PyCPLAC"
consumer_secret = "u6645QwjCmp6zzkGShZHg98HWMkWE55Z2TTfhxqpcFWfjlm678"
access_key = "3170635326-fLPrfjMf8Jdo8WMU6vhVFZ8MgNgO8zsQIG4l8bm"
access_secret = "FlFZMf6oDuWGvSE5zlMu84uinXEIONdRXYv8LkIPOHnV3"


def get_all_tweets(screen_name):
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	alltweets = []

	new_tweets = api.user_timeline(screen_name = screen_name,count=200)

	alltweets.extend(new_tweets)

	oldest = alltweets[-1].id - 1

	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)

		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

		alltweets.extend(new_tweets)

		oldest = alltweets[-1].id - 1

		print "...%s tweets downloaded so far" % (len(alltweets))

	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

	with open('%s_tweets.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)

	pass


if __name__ == '__main__':
	get_all_tweets("@adgpi")
	#get_all_tweets("@ISPR_Official")
	get_all_tweets("@USArmy")
	get_all_tweets("@BritishArmy")
	get_all_tweets("@AustralianArmy")
	get_all_tweets("@mod_russia")
	get_all_tweets("@armeedeterre")
