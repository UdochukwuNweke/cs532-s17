import clusters

def KMeans(k):

	if( k<1 ):
		return

	blognames,words,data=clusters.readfile('blogMatrix.txt')
	kclust=clusters.kcluster(data,k=k)
	clusterCount = 0
	
	print ''
	for cluster in kclust:
		if( len(cluster) > 0 ):
			print 'cluster', clusterCount
			for item in cluster:
				print '\t',blognames[item]
			clusterCount += 1

k=20
KMeans(k)