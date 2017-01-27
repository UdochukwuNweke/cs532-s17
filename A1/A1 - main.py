#curl demonstration
import commands
import sys
from bs4 import BeautifulSoup

def getHeadAttr(attr, head):
	
	head = head.lower()
	indexOfStr = head.find(attr)
	if( indexOfStr != -1 ):
	
		indexOfNewline = head.find('\n', indexOfStr)
		if( indexOfNewline != -1 ):
		
			headAttr = head[indexOfStr:indexOfNewline]
			headAttr = headAttr.replace(attr, '').strip()
			return headAttr.lower()
	
	return -1

def getPDFLinks(links):
	for i in range(0, len(links)):
		head = derefURL_head(links[i])
		if( getHeadAttr('content-type:', head) == 'application/pdf' ):
			print links[i]
			print '\t', i, 'bytesize:', getHeadAttr('content-length:', head)
			print '\ttype: PDF'
			print ''
		
		
		
		
def getLinks(htmlText):
	soup = BeautifulSoup(htmlText, 'html.parser')
	links = soup.findAll('a')
	
	hrefs = []
	for i in range(0, len(links)):
		hrefs.append(links[i]['href'])
		
	return hrefs

def derefURL_head(url):
	co = 'curl  -I -L --silent ' + url
	data = commands.getoutput(co)
	return data
	
def derefURL(url):
	co = 'curl -L --silent ' + url
	data = commands.getoutput(co)
	return data

def curlDemonstration():
	co = 'curl  -i --data "number=17" http://www.numberempire.com/primenumbers.php > output.html'
	data = commands.getoutput(co)
	print data

#A1
#curlDemonstration()

webpage = ''
if len(sys.argv) != 2:
	print 'Invalid arg list'
else:
	#1.
	webpage = sys.argv[1]
	print 'webpage:', webpage
	htmlText = derefURL(url=webpage)
	allLinks = getLinks(htmlText)
	
	'''
	#2.2
	print ''
	print 'all links:'
	for i in range(0, len(allLinks)):
		print(allLinks[i])
	'''
	getPDFLinks(allLinks)