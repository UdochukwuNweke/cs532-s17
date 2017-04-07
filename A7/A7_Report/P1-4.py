import math
from recommendations import *


def euclideanDistance(P, Q):

	if( len(P) != len(Q) ):
		return -1

	sumOfSquares = 0
	for i in range(0, len(P)):
		sumOfSquares += (P[i] - Q[i]) * (P[i] - Q[i])

	return math.sqrt(sumOfSquares)

def getUserDict(path='./data/movielens'):

	users = {}
	occupationMapping = {}
	for line in open(path + '/u.user'):
		(userid, age, gender, occupation, zipcode) = line.split('|')

		userid = userid.strip()
		age = age.strip()
		gender = gender.strip()
		occupation = occupation.strip()
		zipcode = zipcode.strip()

		transformedGender = 1
		if( gender == 'F' ):
			transformedGender = 0

		transformedOccupation = -1
		if( occupation in occupationMapping ):
			transformedOccupation = occupationMapping[occupation]
		else:
			occupationMapping[occupation] = len(occupationMapping)
		
		users.setdefault(userid, {})
		users[userid] = {'userid': userid, 'age': int(age), 'gender': gender,
	   'transformed-gender': 
        transformedGender, 'occupation': occupation, 'transformed-occupation': 
        transformedOccupation, 'zipcode': zipcode}

	return users

def getClosestTriple(users):

	closestTriple = []

	for userid in users:
		
		age = users[userid]['age']
		gender = users[userid]['transformed-gender']
		occupation = users[userid]['transformed-occupation']

		users[userid]['distance'] = euclideanDistance([age, gender, occupation], 
		[32, 0, 5])

	sortedKeys = sorted(users, key=lambda userid:users[userid]['distance'])

	for i in range(0, 3):
		userid = sortedKeys[i]
		closestTriple.append( users[userid] )


	return closestTriple

def question1(users, prefs):

	'''
	1.
	Find 3 users who are closest to you in terms of age, 
	gender, and occupation.  For each of those 3 users:

	- what are their top 3 favorite films?
	- bottom 3 least favorite films?
	'''

	#1 part A:  Find 3 users who are closest to you in terms of age,
	# gender, and occupation.  For each of those 3 users:
	closestTriple = getClosestTriple(users)

	#350, 560, 890
	#1 part B: what are their top 3 favorite films?
	##udoDict = {'transformed-occupation': 5, 'age': 32, 'transformed-gender': 
	#0, 'zipcode': '23508', 'gender': 'F', 'occupation': 'student'}
	for user in closestTriple:
		print('user:', user)
		userRatedMovies = prefs[ user['userid'] ]
		
		topRatedMovies = sorted(userRatedMovies, key=lambda moviename:
		userRatedMovies[moviename])
		
		print('top 3 rated movies:')
		for i in range(len(topRatedMovies)-1, len(topRatedMovies)-4, -1):
			movie = topRatedMovies[i]
			print('\t', i+1, 'movie:', movie, ', rating:', userRatedMovies[movie])

		counter = 3
		if( len(topRatedMovies) < 3 ):
			counter = len(topRatedMovies)

		print('bottom 3 rated movies:')
		for i in range(0, counter):
			movie = topRatedMovies[i]
			print('\t', i+1, 'movie:', movie, ', rating:', userRatedMovies[movie])


		print()

def question2(userid, prefs):

	'''
	2.
	Which 5 users are most correlated to the substitute you? Which
	5 users are least correlated (i.e., negative correlation)?
	'''

	scores = topMatches(prefs, userid, reverseFlag=True)
	print('\n5 Which 5 users are most correlated to user:', userid)
	for scoreUserTuple in scores:
		print('user:', scoreUserTuple[1], ', score:', scoreUserTuple[0])

	scores = topMatches(prefs, userid)
	print('\n5 Which 5 users are least correlated to user:', userid)
	for scoreUserTuple in scores:
		
		print('user:', scoreUserTuple[1], ', score:', scoreUserTuple[0])

def question3(userid, prefs):

	'''
	3.
	Compute ratings for all the films that the substitute you
	have not seen.  Provide a list of the top 5 recommendations for films
	that the substitute you should see.  Provide a list of the bottom
	5 recommendations (i.e., films the substitute you is almost certain
	to hate).
	'''

	#pref with movies userid has not seen
	print('top 5 recommendations for films that the substitute ' + userid + 
	' should see')
	ratings = getRecommendations(prefs, userid)
	for i in range(len(ratings)-1, len(ratings)-6, -1):
		print('\t', ratings[i] )

	print('the bottom 5 recommendations that the substitute ' + userid + 
	' should not see')
	for i in range(0, 5):
		print('\t', ratings[i] )
			
def question4(prefs):

	'''
	4.
	Choose your (the real you, not the substitute you) favorite and
	least favorite film from the data.  For each film, generate a list
	of the top 5 most correlated and bottom 5 least correlated films.
	Based on your knowledge of the resulting films, do you agree with
	the results?  In other words, do you personally like / dislike
	the resulting films?
	'''
	print('most similar for all')
	similarityDict = calculateSimilarItems(prefs, n=5, reverseFlag=True)
	for item, scores in similarityDict.items():
		
		print(item)
		print(scores)
		print()

	print('*'*20)
	print('*'*20)

	print('least similar for all')
	similarityDict = calculateSimilarItems(prefs, n=5, reverseFlag=False)
	for item, scores in similarityDict.items():
		
		print(item)
		print(scores)
		print()


	

users = getUserDict()
prefs = loadMovieLens()

substituteMe = '350'
#question2(substituteMe, prefs)

#question3(substituteMe, prefs)
question4(prefs)

'''
'''
