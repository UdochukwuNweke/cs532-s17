import tweepy
import commands
import time

import os, sys

consumer_key = '01oEm0j9Y52TFtjA5wgRHt9z6'
consumer_secret = 'MWPYnHvrezvhuuFQkOQgnBMYwXZD6SJpnoI8QlE7ZajgQMUKKs'
access_token = '154076252-uK6XnhweIkuc0qIvsNmGiiRebLqvYHbtWDgA5PBi'
access_token_secret = 'LDA5Qel3UQtIwUhvAZLffCGZ9pmmc7wkFOL5k0xx5Yt9O'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def readFromFile(filename):

	infile = open(filename, 'r')
	text = infile.read().strip()
	infile.close()

	return text

def errorMessage():
	exc_type, exc_obj, exc_tb = sys.exc_info()
	fname = os.path.split(exc_tb.tb_frame.f_code.co_filename[1])
	print fname, str(exc_tb.tb_lineno), str(sys.exc_info())

def unshortenURL(url):

	curlRequest = 'curl -IL --silent ' + url + ' | egrep -i "(HTTP/1.1|^location:)"'
	curlOutput = commands.getoutput(curlRequest)
	curlOutput = curlOutput.splitlines()

	if( len(curlOutput) < 2 ):
		return ''
	
	
	if( curlOutput[-1].lower() == 'http/1.1 200 ok' ):
		return curlOutput[-2].split(' ')[-1].strip()


	return ''

def getLinksFromTweets():

	searchKeys = []
	stopProgramFlag = 'false'
	sinceID = {}

	try:
		while(True):
		
			stopProgramFlag = readFromFile('./stopProgramChk.txt')
			searchKeys = readFromFile('./searchKeys.txt').split(',')

			if( stopProgramFlag == 'true' ):
				break

			
			print 'stopProgramFlag:', stopProgramFlag
			print 'searchKeys:', searchKeys

			for searckKey in searchKeys:
				searchKey = searckKey.strip()
				print '\n...searching for:', searckKey

				if( searchKey not in sinceID ):
					sinceID[searchKey] = 0

				print 'sinceID:', sinceID[searchKey]

				outfile = open('./allTweets.txt', 'a')
				

				
				outfile.close()

				print '...sleeping for 15 seconds'
				time.sleep(15)


	except:
		errorMessage()


	

def removeDups():

	infile = open('allTweets.txt', 'r')
	lines = infile.readlines()
	infile.close()

	dedupDict = {}

	print 'len(lines):', len(lines)

	for line in lines:
		line = line.strip()

		line = line.split(' <**> ')
		
		if( len(line) < 1 ):
			continue

		id = line[0]
		url = line[1]

	
		dedupDict[url] = id
		#print(line)

	print 'len(dedupDict):', len(dedupDict)
	outfile = open('allTweets.txt', 'w')
	
	counter = 0
	for url, id in dedupDict.items():

		try:
			'''
			Final url is unshortened 
			'''
			counter += 1
			print '\tcounter:', counter
			url = unshortenURL(url).strip()
			print '\turl:', url

			if( len(url) == 0 ):
				continue

			outfile.write( url + '\n')

			print ''
		except:
			errorMessage()
		

	outfile.close()

		
if __name__ == '__main__':
	#getLinksFromTweets()
	removeDups()