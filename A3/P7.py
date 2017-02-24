import os
import commands
from P1 import getUniqueURLs
from P1 import errorMessage

def getInvertedFile(lines, vocabulary):

	counter = 0
	for term, value in vocabulary.items():

		invertedLine = ''
		for i in range(0, len(lines)):

			try:
				print i, 'of', len(lines)
				print 'term:', term
				print 'counter:', counter, 'of', len(vocabulary)
				print ''

				url = lines[i].strip()
				filename = './Text/' + str(i) + '.txt'

				if( os.path.exists(filename) == False ):
					continue

				co = 'cat ' + filename + ' | grep -icw "' + term + '"'
				output = int(commands.getoutput(co).strip())
				if( output > 0 ):
					invertedLine = invertedLine + ', ' + str(i)

			except:
				errorMessage()

		if( len(invertedLine) != 0 ):
			if( invertedLine.strip()[0] == ',' ):
				invertedLine = invertedLine[1:]

			invertedLine = term + ': ' + invertedLine
			try:
				outfile = open('./invertedFile.txt', 'a')
				invertedLine = invertedLine.encode('utf-8')
				outfile.write(invertedLine + '\n')
				outfile.close()
			except:
				errorMessage()
		
		
		#if (counter == 10):
		#	break

		counter += 1

def getVocabulary(lines):
	
	vocabulary = {}
	for i in range(0, len(lines)):

		print i
		url = lines[i].strip()
		filename = './Text/' + str(i) + '.txt'

		if( os.path.exists(filename) == False ):
			continue

		co = 'cat ' + filename
		output = commands.getoutput(co)
		output = output.lower()
		output = output.split(' ')

		for term in output:
			term = term.strip()

			if( len(term) != 0 ):
				vocabulary[term] = True


	return vocabulary


lines = getUniqueURLs()
vocabulary = getVocabulary(lines)

getInvertedFile(lines, vocabulary)