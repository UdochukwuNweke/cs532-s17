from numpredict import knnestimate, cosineDistance

def readfile(filename):
	return do_readfile(open(filename).readlines())

def do_readfile(lines):
	colnames = lines[0].strip().split('\t')[1:]
	rownames = []
	data = []

	for line in lines[1:]:
		p = line.strip().split('\t')
		rownames.append(p[0])
		data.append([float(x) for x in p[1:]])

	return rownames, colnames, data

def createVectorData(blognames, data):
	
	if( len(blognames) != len(data) ):
		print('mismatch exiting')
		return

	vectors = []
	for i in range(0, len(blognames)):

		blogDict = {}
		blogDict['name'] = blognames[i]
		blogDict['input'] = data[i]
		blogDict['result'] = 0
		vectors.append(blogDict)

	return vectors

def getIntFromList(lst):

	lst = lst.split('\t')
	for i in range(0, len(lst)):
		lst[i] = int(lst[i])

	return lst


webSciDLVector = '8	39	1	286	2	175	194	65	0'	
webSciDLVector = getIntFromList(webSciDLVector)

fMeasureVector = '1	4	4	1	3	23	1	9	5'	
fMeasureVector = getIntFromList(fMeasureVector)

blognames, words, data = readfile('./blogMatrix.txt')
vectors = createVectorData(blognames, data)

k = 5
knnestimate(vectors, fMeasureVector, k+1)
