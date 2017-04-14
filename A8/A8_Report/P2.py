import clusters#from:https://raw.githubusercontent.com/nico/
#collectiveintelligence-book/master/clusters.py
import drawclust

def generateASCIIDendogram(filename):
	blognames,words,data=clusters.readfile(filename)
	clust=clusters.hcluster(data)
	clusters.printclust(clust,labels=blognames)

def generateJPegDendogram(filename):
	blognames,words,data=clusters.readfile(filename)
	clust=clusters.hcluster(data)
	drawclust.drawdendogram(clust,blognames,filename + '.jpg')



filename = './blogMatrix.txt'
#P2.a 
#generateASCIIDendogram(filename)

#P2.a 
#generateJPegDendogram(filename)