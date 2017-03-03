from util import *

from os.path import dirname, abspath
from bs4 import BeautifulSoup

def workingFolder():
	return dirname(abspath(__file__)) + '/'

def getFriendCountDict(friendsTxt):

	friendsDict = {}
	problematicFriendsCount = 0
	try:
		soup = BeautifulSoup(friendsTxt, 'xml')
		graph = soup.find('graph')

		if( graph is not None ):
			nodes = graph.findAll('node')

			for node in nodes:
				try:
					friendName = node.find('data', {'key': 'Label'}).text
					friendCount = node.find('data', {'key': 'friend_count'}).text
					friendsDict[ node['id'] ] = {'friend_name': friendName,
					'friend_count'
					: int(friendCount)}
				except:
					errorMsg()
					problematicFriendsCount += 1
	except:
		errorMsg()

	print('\nfriendsDict.len:', len(friendsDict))
	print('problematicFriendsCount:', problematicFriendsCount, '\n')
	sortedIDs = sorted(friendsDict, key=lambda x: friendsDict[x]['friend_count'])

	try:
		outfile = open('./mlnFriends.csv', 'w')

		outfile.write('Friend,FriendsCount\n')
		for friendID in sortedIDs:
			print(friendsDict[friendID]['friend_name'], friendsDict[friendID]
				['friend_count'])
			outfile.write( friendsDict[friendID]['friend_name'] + ', ' + 
				str(friendsDict[friendID]['friend_count']) + '\n' )

		outfile.close()
	except:
		errorMsg()

friendsTxt = readTextFromFile(workingFolder() + 'mlnFriends.xml')
getFriendCountDict(friendsTxt)