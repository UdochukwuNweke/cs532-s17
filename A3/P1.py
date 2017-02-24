import commands
import os, sys
from bs4 import BeautifulSoup

import re
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

#from nltk: https://github.com/nltk/nltk/commit/39a303e5ddc4cdb1a0b00a3be426239b1c24c8bb
def clean_html(html):

	# First we remove inline JavaScript/CSS:
	cleaned = re.sub(r"(?is)<(script|style).*?>.*?(</\1>)", "", html.strip())
	# Then we remove html comments. This has to be done before removing regular
	# tags since comments can contain '>' characters.
	cleaned = re.sub(r"(?s)<!--(.*?)-->[\n]?", "", cleaned)
	# Next we can remove the remaining tags:
	cleaned = re.sub(r"(?s)<.*?>", " ", cleaned)
	# Finally, we deal with whitespace
	cleaned = re.sub(r"&nbsp;", " ", cleaned)
	cleaned = re.sub(r"  ", " ", cleaned)
	cleaned = re.sub(r"  ", " ", cleaned)

	#my addition to remove blank lines
	cleaned = re.sub("\n\s*\n*", "\n", cleaned)

	return cleaned.strip()

def saveTextToFile(filename, text):
	try:
		outfile = open(filename, 'w')
		outfile.write(text)
		outfile.close()
	except:
		errorMessage()

def derefURL(url):

	try:
		co = 'curl -L --silent -m 20 "' + url + '"'
		data = commands.getoutput(co)
		return data
	except:
		errorMessage()
		return ''

def errorMessage():
	exc_type, exc_obj, exc_tb = sys.exc_info()
	fname = os.path.split(exc_tb.tb_frame.f_code.co_filename[1])
	print fname, str(exc_tb.tb_lineno), str(sys.exc_info())

def getUniqueURLs():

	infile = open('./1000UniqueURLs.txt', 'r')
	lines = infile.readlines()
	infile.close()

	return lines

def saveRawHTML(lines):

	for i in range(0, len(lines)):
		
		textOutfilename = './Text/' + str(i) + '.txt'
		#if( os.path.exists(textOutfilename) == True ):
		#	continue

		url = lines[i].strip()
		html = derefURL(url)

		if( len(html) != 0 ):
			
			try:
				#soup = BeautifulSoup(html, 'html.parser')
				#text = soup.get_text()
				text = clean_html(html)
				if( len(text) != 0 ):
					saveTextToFile(textOutfilename, text)
					print '\tsaved text', len(text)
					
			except:
				errorMessage()

			try:
				saveTextToFile('./RawHTML/' + str(i) + '.html', html)
				print '\tsaved html'
			except:
				errorMessage()

		print i

if __name__ == '__main__':
	
	lines = getUniqueURLs()
	saveRawHTML(lines)