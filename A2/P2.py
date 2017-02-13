
import commands
from P1 import errorMessage, readFromFile
import json
import os

def downloadTimemap(url):

	try:
		curlRequest = 'curl --silent http://memgator.cs.odu.edu/timemap/json/' + url
		curlOutput = commands.getoutput(curlRequest)
		return curlOutput
	except:
		errorMessage()
		return ''

def saveText(filename, text):

	try:
		outfile = open(filename, 'w')
		outfile.write(text)
		outfile.close()
	except:
		errorMessage()

def getUniqueURLs():

	infile = open('./1000UniqueURLs.txt', 'r')
	lines = infile.readlines()
	infile.close()

	return lines

def downloadTimemapsAndSave(urls):

	for i in range(0, len(lines)):
		url = lines[i].strip()
		print i, url

		timemapText = downloadTimemap(url)

		try:
			json.loads(timemapText)

			filename = './Timemaps/' + str(i) + '.json'
			saveText(filename, timemapText)

			print '\tsaved filename:', filename
		except:
			errorMessage()

		print ''

def countMementos(urls):

	outfile = open('./MementoCounts.csv', 'w')
	outfile.write('ID,MementoCount\n')

	for i in range(0, len(lines)):
		url = lines[i].strip()
		print i, url

		try:

			filename = './Timemaps/' + str(i) + '.json'
			if( os.path.exists(filename) != True ):
				continue

			timemapText = readFromFile(filename)
			timemapText = json.loads(timemapText)
			
			memCount = len(timemapText['mementos']['list'])
			print '\tmemCount:', memCount
			outfile.write(str(i) + ', ' + str(memCount) + '\n')
		except:
			errorMessage()

		print ''

	outfile.close()

if __name__ == '__main__':
	lines = getUniqueURLs()
	#downloadTimemapsAndSave(lines)

	countMementos(lines)