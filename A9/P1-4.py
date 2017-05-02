import os, sys
import docclass
import feedparser
import feedfilter
from subprocess import check_output

def errorMsg():
	exc_type, exc_obj, exc_tb = sys.exc_info()
	fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
	print(fname, exc_tb.tb_lineno, sys.exc_info())

def FisherModel(trainingInputFileName, entriesXMLFileName, dbFileName, mode, maxItems):
	#input: trainingInputFileName.txt, entriesXMLFileName.xml, mode is 'test' or 'train', 'getWord'|'getEntry'
	
	cl=docclass.fisherclassifier(docclass.getwords)
	'''
	if( getWordGetEntryMethod == 'getWord' ):
		cl=docclass.fisherclassifier(docclass.getwords)
	else:
		cl=docclass.fisherclassifier(feedfilter.entryfeatures)
	'''

	
	cl.setdb(dbFileName)
	feedfilter.getClassData(entriesXMLFileName, cl, trainingInputFileName, mode, maxItems)

def downloadBlogXML(blogUrl, outputFilename, countToProcess):

	try:
		
		output = check_output(['curl', '-s', blogUrl + 'feeds/posts/default?max-results=' + str(countToProcess)])
		output = output.decode('utf-8')

		outputFile = open(outputFilename, 'w')
		outputFile.write(output)
		outputFile.close()
	except:
		print('Error parsing feed %s' % blogUrl)
		errorMsg()

#problem 1:
blogName = 'icovetthee'
blogUrl = 'http://www.' + blogName + '.com/'
xmlOutputFilename = './' + blogName + '.xml'
#download 10 feeds from blogUrl and save into xml file called blog.xml
#downloadBlogXML(blogUrl, xmlOutputFilename, 120)


#problem 2 (training):
trainingCount = 50
dboutputFileName = blogName +'.db'
trainingInputfilename = 'Training-50Entries.txt'
#FisherModel(trainingInputfilename, xmlOutputFilename, dboutputFileName, 'train', trainingCount)

#problem 2 (testing):
trainingInputfilename = 'Testing-50Entries.txt'
#FisherModel(trainingInputfilename, xmlOutputFilename, dboutputFileName, 'test', trainingCount)


#problem 3 (training):
dboutputFileName = blogName +'.90.db'
#FisherModel('Training-90Entries.txt', xmlOutputFilename, dboutputFileName, 'train', 90)

#problem 3 (testing):
#FisherModel('Testing-10Entries.txt', xmlOutputFilename, dboutputFileName, 'test', 10)

