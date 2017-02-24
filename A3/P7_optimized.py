import os, sys
from subprocess import check_output


def errorMessage():
	exc_type, exc_obj, exc_tb = sys.exc_info()
	fname = os.path.split(exc_tb.tb_frame.f_code.co_filename[1])
	print(fname, str(exc_tb.tb_lineno), str(sys.exc_info()))

def getUniqueURLs():

	infile = open('./1000UniqueURLs.txt', 'r')
	lines = infile.readlines()
	infile.close()

	return lines
def getInvertedFile(lines, vocabulary, multipleVocabs):

	counter = 0
	for term, value in vocabulary.items():

		invertedLine = ''
		for i, docVocabDict in multipleVocabs.items():

			try:

				print(i, 'of', len(multipleVocabs))
				print('term:', term)
				print('counter:', counter, 'of', len(vocabulary))
				print('')

				if( term in multipleVocabs[i] ):
					invertedLine = invertedLine + ', ' + str(i)

			except:
				errorMessage()

		if( len(invertedLine) != 0 ):
			if( invertedLine.strip()[0] == ',' ):
				invertedLine = invertedLine[1:]

			invertedLine = term + ': ' + invertedLine
			try:
				outfile = open('./invertedFile_good.txt', 'a')
				outfile.write(invertedLine + '\n')
				outfile.close()
			except:
				errorMessage()

		counter += 1

def getVocabulary(lines):
	
	vocabulary = {}
	multipleVocabs = {}
	for i in range(0, len(lines)):

		try:
			multipleVocabs[i] = {}
			print(i)
			url = lines[i].strip()
			filename = './Text/' + str(i) + '.txt'

			if( os.path.exists(filename) == False ):
				continue

			output = check_output(['cat', filename])
			output = output.decode('utf-8')
			output = output.lower().split(' ')

			for term in output:
				term = term.strip()

				if( len(term) != 0 ):
					vocabulary[term] = True
					multipleVocabs[i][term] = True
		except:
			errorMessage()


	return vocabulary, multipleVocabs


lines = getUniqueURLs()
vocabulary, multipleVocabs = getVocabulary(lines)

getInvertedFile(lines, vocabulary, multipleVocabs)