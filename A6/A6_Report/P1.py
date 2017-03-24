from util import *
import tweepy
import json
import time

consumer_key = '01oEm0j9Y52TFtjA5wgRHt9z6'
consumer_secret = 'MWPYnHvrezvhuuFQkOQgnBMYwXZD6SJpnoI8QlE7ZajgQMUKKs'
access_token = '154076252-uK6XnhweIkuc0qIvsNmGiiRebLqvYHbtWDgA5PBi'
access_token_secret = 'LDA5Qel3UQtIwUhvAZLffCGZ9pmmc7wkFOL5k0xx5Yt9O'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def writeFollowers(response, friendsDict):

	for follower in response:
		friendsDict[follower.screen_name] = follower.name

def getLink(source_screen_name, source_name, target_screen_name, target_name, outfile):
	link = api.show_friendship(source_screen_name=source_screen_name, 
	target_screen_name=target_screen_name)
	
	if( link[0].following ):
		print('\t\t', source_name, 'follows', target_name)
		#graphEdges.append( {'source': source_name, 'target': target_name} )
		outfile.write('{"source": "' + source_name + '", 
		"target": "' + target_name + '"},\n')

	if( link[0].followed_by ):
		print('\t\t', target_name, 'follows', source_name)
		
		#graphEdges.append( {'source': target_name, 'target': source_name} )
		outfile.write('{"source": "' + target_name + '", 
		"target": "' + source_name + '"},\n')

def writeFirstDegreeLinks(outfile):

	followersList = readTextFromFile('./phonedude_mln.followers.array.json')
	followersList = json.loads(followersList)

	for follower in followersList:
		outfile.write('{"source": "Michael L. Nelson", "target":
		 "' + follower['name'] + '"},\n')


def computeFriendshipLink(outfile):

	followersList = readTextFromFile('./phonedude_mln.followers.array.json')
	followersList = json.loads(followersList)

	counter = 0
	for i in range(9, 100):
		for j in range(i+1, len(followersList)):
			source_screen_name = followersList[i]['screen-name']
			target_screen_name = followersList[j]['screen-name']

			source_name = followersList[i]['name']
			target_name = followersList[j]['name']

			print('\t', source_screen_name, source_name )
			print('\t', target_screen_name, target_name )
			
			getLink(source_screen_name=source_screen_name, source_name=source_name, 
			target_screen_name=target_screen_name, 
			target_name=target_name, outfile=outfile)
			

			print('\t', i, j)
			print('\tsleeping')
			time.sleep(6)
			
			counter += 1
		print('\n'*4)

	print('counter:', counter)


def getFriendsDict(twitterName):

	try:
		rateLimitQuota = api.rate_limit_status()['resources']['followers']
		['/followers/list']['remaining']
		print('\trateLimitQuota:', rateLimitQuota)


		twitterAccount = api.get_user(twitterName)
		#followersCount = int(twitterAccount._json['friends_count'])
		
		followersDict = {}
		response = twitterAccount.followers(count=200, cursor=-1)
		nextCursor = response[1][1]
		writeFollowers(response[0], followersDict)
		
		for i in range(0, 3):
			response = twitterAccount.followers(count=200, cursor=nextCursor)
			nextCursor = response[1][1]
			writeFollowers(response[0], followersDict)
		

		writeDictToJson('./phonedude_mln.followers.json', followersDict)

	
	except:
		errorMsg()

#getFriendsDict('phonedude_mln')


outfile = open('./friendshipGraph.json', 'a')

#outfile.write('[\n')
#writeFirstDegreeLinks(outfile)

computeFriendshipLink(outfile)


outfile.write(']')
outfile.close()