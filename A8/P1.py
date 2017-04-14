import os, sys
import requests
import time

from mod_generatefeedvector import generateFeedVector

def errorMsg():
	exc_type, exc_obj, exc_tb = sys.exc_info()
	fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
	print(fname, exc_tb.tb_lineno, sys.exc_info() )

def getTerminalBlog(blogURL):

	try:
		r = requests.head(blogURL, allow_redirects=True)
		return r.url.replace('?expref=next-blog', '')
	except:
		errorMsg()

	return ''


def getBlogs(countOfBlogs):

	if( countOfBlogs < 1 ):
		print('Invalid input for count of blogs')
		return

	try:
		output = open('unique100Blogs.txt', 'w')
		output.write('http://f-measure.blogspot.com/\n')
		output.write('http://ws-dl.blogspot.com/\n')
	except:
		errorMsg()

	blogDict = {}
	while len(blogDict) < countOfBlogs:
		
		blogUrl = 'http://www.blogger.com/next-blog?navBar=true&blogID=5885297259923277298'
		terminalBlogURL = getTerminalBlog(blogUrl)
		
		if( len(terminalBlogURL) != 0 ):
			print('count:', len(blogDict) )
			print('blog:', terminalBlogURL)
			blogDict[terminalBlogURL] = False

		print('\tsleeping')
		print()
		time.sleep(3)

	
	for url in blogDict:
		output.write(url + '\n')

	output.close()

#1a
#getBlogs(200)

#1b
generateFeedVector(100)#generate blogMatrix.txt