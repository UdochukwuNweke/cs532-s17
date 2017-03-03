from util import *
import tweepy
import json

consumer_key = '01oEm0j9Y52TFtjA5wgRHt9z6'
consumer_secret = 'MWPYnHvrezvhuuFQkOQgnBMYwXZD6SJpnoI8QlE7ZajgQMUKKs'
access_token = '154076252-uK6XnhweIkuc0qIvsNmGiiRebLqvYHbtWDgA5PBi'
access_token_secret = 'LDA5Qel3UQtIwUhvAZLffCGZ9pmmc7wkFOL5k0xx5Yt9O'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def writeFollowers(response, friendsDict):

	for follower in response:
		friendsDict[follower.screen_name] = follower.followers_count
		

def getFriendsDict(twitterName):

	try:
		rateLimitQuota = api.rate_limit_status()['resources']['friends']
		['/friends/list']['remaining']
		print('\trateLimitQuota:', rateLimitQuota)


		twitterAccount = api.get_user(twitterName)
		#followersCount = int(twitterAccount._json['friends_count'])
		
		friendsDict = {}
		response = twitterAccount.friends(count=200, cursor=-1)
		nextCursor = response[1][1]
		writeFollowers(response[0], friendsDict)
		
		response = twitterAccount.friends(count=200, cursor=nextCursor)
		writeFollowers(response[0], friendsDict)

		sortedIDs = sorted(friendsDict, key=lambda x: friendsDict[x])
		outfile = open('./twitter.mlnFriends.csv', 'w')

		outfile.write('Friend,FriendsCount\n')
		for screen_name in sortedIDs:
			print(screen_name, friendsDict[screen_name])
			outfile.write( screen_name + ', ' + str(friendsDict[screen_name]) + '\n' )

		outfile.close()
	
	except:
		errorMsg()

getFriendsDict('phonedude_mln')