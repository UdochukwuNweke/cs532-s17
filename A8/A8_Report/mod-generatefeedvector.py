import os, sys
import feedparser
import re
import requests
from bs4 import BeautifulSoup


def errorMsg():
	exc_type, exc_obj, exc_tb = sys.exc_info()
	fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
	print(fname, exc_tb.tb_lineno, sys.exc_info() )

def getwords(html):
	# Remove all the HTML tags
	txt = re.compile(r'<[^>]+>').sub('', html)

	# Split words by all non-alpha characters
	words = re.compile(r'[^A-Z^a-z]+').split(txt)

	# Convert to lowercase
	return [word.lower() for word in words if word != '']

def mergeDicts(dictA, dictB):

	for term, TF in dictB.items():

		if( term in dictA ):
			dictA[term] = dictA[term] + TF
		else:
			dictA[term] = TF

	return dictA
	

def getPagesForBlog_main(blogUrl, pages=[]):

	try:
		html = requests.get(blogUrl)
		soup = BeautifulSoup(html.text, 'html.parser')
		nextLink = soup.find('link', { 'rel' : 'next' })

		if nextLink is not None:
			nextLink = nextLink['href']
			pages.append(nextLink)
			getPagesForBlog_main(nextLink, pages)

	except:
		errorMsg()

	return pages

def getPagesForBlog_pre(blogUrl):

	blogUrl = blogUrl.strip()
	pages = []
	
	if( blogUrl[-1:] != '/' ):
		blogUrl = blogUrl + '/feeds/posts/default?max-results=500'
	else:
		blogUrl = blogUrl + 'feeds/posts/default?max-results=500'

	pages = getPagesForBlog_main(blogUrl, pages)

	return pages

def getwordcounts(url):
	'''
	Returns title and dictionary of word counts for an RSS feed
	'''
	# Parse the feed


	#url: http://blogName.blogspot.com/
	d = feedparser.parse(url)
	wc = {}

	# Loop over all the entries
	for e in d.entries:
		if 'summary' in e:
			summary = e.summary
		else:
			summary = e.description

		# Extract a list of words
		words = getwords(e.title + ' ' + summary)
		for word in words:
			wc.setdefault(word, 0)
			wc[word] += 1

	return (d.feed.title, wc)

#modified to look at all pages of the blog
def generateFeedVector(blogCount=10):

	if( blogCount < 1 ):
		return

	apcount = {}
	wordcounts = {}

	infile = open('./unique100Blogs.txt', 'r')
	feedlist = infile.readlines()
	infile.close()

	counter = 1
	for feedurl in feedlist:

		print('counter: ', counter)
		
		feedurl = feedurl.strip()

		try:
			#before: (title, wc) = getwordcounts(feedurl + 'feeds/posts/default/')
			#after:
			(title, wc) = getwordcounts(feedurl + 
			'feeds/posts/default?max-results=500')

			#get wc for other pages - start
			otherPages = getPagesForBlog_pre(feedurl)
			for page in otherPages:
				page = page.strip()
				(sameTitle, nextPageWordCount) = getwordcounts(page)
				mergeDicts(wc, nextPageWordCount)
			#get wc for other pages - end

			#wc is union
			wordcounts[title] = wc
			for (word, count) in wc.items():
				apcount.setdefault(word, 0)
				if count > 1:
					apcount[word] += 1
		except:
			print('Failed parsing for feed %s' % feedurl)
			errorMsg()

		if( blogCount == counter ):
			break

		counter += 1


	wordlist = []
	TermTermFrequencyTuplesList = []
	for (term, termFrequency) in apcount.items():

		frac = float(termFrequency) / len(feedlist)

		if frac > 0.1 and frac < 0.5:
			termTermFrequencyTuple = (term, termFrequency)
			TermTermFrequencyTuplesList.append(termTermFrequencyTuple)


	#Limit the number of terms to the most "popular" (i.e., frequent) 1000 terms
	TermTermFrequencyTuplesList = sorted(TermTermFrequencyTuplesList, key=lambda tup:
    tup[1], reverse=True)	
	for termFrequencyTuple in  TermTermFrequencyTuplesList:

		#get 1000 most popular terms
		if( len(wordlist) <= 1000 ):
			wordlist.append( termFrequencyTuple[0] )
		else:
			break
	

	out = open('blogMatrix.txt', 'w')
	out.write('Blog')

	for word in wordlist:
		out.write('\t%s' % word)

	out.write('\n')
	for (blog, wc) in wordcounts.items():
		
		#print blog
		out.write(blog)
		for word in wordlist:

			if word in wc:
				out.write('\t%d' % wc[word])
			else:
				out.write('\t0')
		out.write('\n')

	out.close()