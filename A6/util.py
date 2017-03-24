import os, sys
import json

def errorMsg():
	exc_type, exc_obj, exc_tb = sys.exc_info()
	fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
	errorMsg = fname + ', ' + str(exc_tb.tb_lineno) + ', ' + str(sys.exc_info())
	print('\tError:', errorMsg)

def readTextFromFile(filename):
	
	text = ''
	try:
		infile = open(filename, 'r')
		text = infile.read()
		infile.close()
	except:
		errorMsg()

	return text

def writeDictToJson(filename, inputDict):

	try:
		outfile = open(filename, 'w')
		json.dump(inputDict, outfile)
		outfile.close()
	except:
		errorMsg()