import commands
import json
import os, sys
from datetime import datetime

def errorMessage():
	exc_type, exc_obj, exc_tb = sys.exc_info()
	fname = os.path.split(exc_tb.tb_frame.f_code.co_filename[1])
	print fname, str(exc_tb.tb_lineno), str(sys.exc_info())

def getUniqueURLs():

	infile = open('./1000UniqueURLs.txt', 'r')
	lines = infile.readlines()
	infile.close()

	return lines

def getCreationDateForURI(url):

	try:
		dockerRequest = 'docker run --rm -it carbon ./main.py -l search ' + url
		dockerOutput = commands.getoutput(dockerRequest)

		indexOfBrace = dockerOutput.find('{')
		if( indexOfBrace == -1 ):
			return ''

		dockerOutput = dockerOutput[indexOfBrace:]
		dockerOutput = json.loads(dockerOutput)

		return dockerOutput['Estimated Creation Date']
	except:
		errorMessage()
		return ''


def getCreationDates(urls):

	outfile = open('./CreationDates.csv', 'a')

	for i in range(0, len(lines)):
		url = lines[i].strip()
		print i, url

		try:
			creationDate = getCreationDateForURI(url)
		
			if( len(creationDate) == 0 ):
				continue

			creationDateObj = datetime.strptime(creationDate, '%Y-%m-%dT%H:%M:%S')
			delta = datetime.now() - creationDateObj
			print 'age: ', delta

			outfile.write(str(i) + ', ' + str(delta.days) + '\n')
		except:
			errorMessage()

		print ''

	outfile.close()

def matchMementoCountWithCreationDates():

	memCountLines = []
	ageLines = []

	try:
		infile = open('../MementoCounts.csv', 'r')
		memCountLines = infile.readlines()
		del memCountLines[0]
		infile.close()

		infile = open('./CreationDates.csv', 'r')
		ageLines = infile.readlines()
		del ageLines[0]
		infile.close()
	except:
		errorMessage()
		return

	#key is URL ID, value is MementoCounts
	memCountDict = {}

	#key is URL ID, value is Age
	ageDict = {}


	memCountAgeDict = {}

	for line in memCountLines:
		IDMemCount = line.split(', ')
		memCountDict[ IDMemCount[0].strip() ] = IDMemCount[1].strip()

	for line in ageLines:
		IDAge = line.split(', ')
		ageDict[ IDAge[0].strip() ] = IDAge[1].strip()


	for ID, memCount in memCountDict.items():
		if( ID in ageDict ):
			memCountAgeDict[ID] = { 'memCount': memCount, 'age': ageDict[ID] }


	print 'ID,MementoCount,Age'
	for ID, memCountAge in memCountAgeDict.items():
		toPrint = ID + ', ' + memCountAge['memCount'] + ', ' + memCountAge['age']
		print toPrint

#lines = getUniqueURLs()
#getCreationDates(lines)

matchMementoCountWithCreationDates()