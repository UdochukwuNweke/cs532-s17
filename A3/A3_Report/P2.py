from P1 import getUniqueURLs
from P1 import errorMessage
import os
import commands
import math

def searchForTermInFiles(lines, key):

	count = 0
	for i in range(0, len(lines)):

		print i
		url = lines[i].strip()
		filename = './Text/' + str(i) + '.txt'

		if( os.path.exists(filename) == False ):
			continue

		co = 'cat ' + filename + ' | grep -i -w ' + key
		output = commands.getoutput(co)
		#output = output.strip()

		if( len(output) != 0 ):
			print '\tFound'
			print '\t', url
			count += 1

		#if( count == 10 ):
		#	break

	print 'found count:', count
	print 'key:', key

def calculateTFIDFForIndex(lines, docsWithTerm, key, idfvalue):
	
	print 'TF-IDF for key:', key
	for docIndex in docsWithTerm:
	
		url = lines[docIndex].strip()
		filename = './Text/' + str(docIndex) + '.txt'
		
		co = 'cat ' + filename + ' | grep -icw ' + key

		try:
			output = commands.getoutput(co)
			wordCount = int(output)

			co = 'wc -w ' + filename
			totalWords = commands.getoutput(co)
			totalWords = int(totalWords.split(' ')[0].strip())

			tf = 0
			if( totalWords > 0 ):
				tf = round(wordCount/float(totalWords), 4)

			print url
			#print filename
			print 'wordCount:', wordCount
			print 'totalWords:', totalWords
			print 'tf:', tf
			print 'idf:', IDF
			print 'tfidf:', round(tf * IDF, 4)


		except:
			errorMessage()

		print ''

		

lines = getUniqueURLs()

key = 'Russia'
#searchForTermInFiles(lines, key)

#IDF = 1000 docs / 93 documents with term Russia, IDF = log2(1000/93): 3.4266 
IDF = 3.4266
docsWithTerm = [5, 6, 7, 11, 13, 19, 20, 25, 26, 68]
calculateTFIDFForIndex(lines, docsWithTerm, key, IDF)