import clusters
import drawclust

def MDS():
	iterations = 0
	blognames,words,data=clusters.readfile('blogMatrix.txt')
	coords, iterations=clusters.scaledown(data)
	drawclust.draw2d(coords,blognames,'blogMatrix.mds.jpg')

	print 'iterations', iterations

MDS()