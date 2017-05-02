from numpredict import knnestimate, cosineDistance

#from clusters.py in https://raw.githubusercontent.com/nico/collectiveintelligence-book/master/clusters.py
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

webSciDLVector = '8	39	1	286	2	175	194	65	0	348	2	5	4	12	9	25	1	33	0	13	8	34	45	55	6	0	79	0	38	92	5	19	8	9	50	6	1	17	104	0	51	16	0	19	1	805	0	17	0	15	8	2	1	5	12	5	11	47	21	33	2	12	3	189	94	16	9	7	1	54	2	2	4	1	0	3	31	31	12	11	3	1	0	26	1	3	28	3	20	5	0	83	28	24	4	28	10	8	21	56	2	13	37	7	23	1	2	5	64	3	32	1	21	7	14	2	4	20	3	49	0	222	2	9	15	41	22	0	3	10	24	98	2	13	4	6	0	34	4	6	24	19	2	0	15	2	17	19	10	0	25	22	11	8	27	19	0	0	113	9	16	15	0	11	28	19	2	309	48	33	0	1	4	3	4	44	57	411	4	9	3	3	3	45	10	13	57	27	0	2	7	4	11	0	0	10	115	23	4	7	149	171	53	20	23	15	4	0	45	31	12	16	25	6	7	34	5	11	2	14	1	13	20	0	0	24	20	25	17	3	3	8	7	1	29	3	23	3	0	11	56	0	4	10	0	1	0	16	4	25	3	239	10	39	7	39	12	26	0	10	21	9	1	64	3	23	218	25	0	3	1	46	2	7	4	36	0	2	17	2	4	25	1	0	5	24	2	15	16	21	1	1	0	16	0	18	47	4	7	8	0	52	2	30	2	17	3	15	67	7	16	3	3	12	0	3	9	1	26	2	0	7	10	14	9	1	0	32	37	84	21	30	12	20	9	5	5	17	9	2	0	138	11	14	0	2	6	27	8	2	1	7	2	104	3	16	58	8	1	2	0	107	11	1	1	3	19	41	17	6	0	20	3	6	0	15	24	3	16	66	0	30	10	1	0	6	6	0	62	0	1	1	3	102	3	2	3	6	35	0	22	1	18	20	60	37	11	23	36	16	23	0	4	27	43	4	0	34	3	9	13	4	171	8	12	22	15	0	2	6	6	0	4	2	1	4	6	7	18	1	39	102	25	1	48	11	0	22	2	14	9	6	0	1	0	0	3	2	12	35	0	69	14	0	5	23	14	17	5	7	10	10	5	4	0	25	14	5	4	7	13	0	4	3	6	15	14	2	28	38	2	7	1	12	5	14	1	7	2	5	10	1	2	8	17	1	0	19	0	11	12	0	18	1	1	0	0	22	3	2	41	0	5	1	27	0	7	16	0	27	0	9	28	170	2	0	0	5	2	2	46	17	5	1	27	8	1	2	4	5	0	0	4	2	24	12	0	4	4	250	8	1	18	11	0	6	21	13	8	6	1	33	1	3	13	0	7	56	1	13	0	0	4	0	1	5	14	3	54	4	4	9	6	46	9	3	0	2	1	4	11	437	2	0	0	2	7	0	2	0	34	4	12	3	2	0	18	0	0	3	8	22	5	0	0	14	3	8	0	3	26	0	17	4	178	16	4	15	3	14	29	4	26	0	0	20	2	0	6	2	8	6	0	37	20	2	0	0	2	0	1	2	5	47	5	1	25	3	7	1	1	22	6	111	13	2	0	30	8	3	18	0	2	1	18	0	0	0	416	1	7	0	4	6	30	0	0	3	0	1	15	9	18	0	31	15	37	0	0	25	20	82	1	0	3	9	11	12	7	4	4	14	1	42	12	2	0	41	0	22	25	1	30	9	5	10	0	1	10	29	3	4	16	14	3	17	4	26	5	12	3	39	0	21	20	3	8	2	2	3	0	1	493	2	6	12	11	1	5	1	36	14	0	2	2	16	7	0	13	0	0	5	1	11	1	49	0	1	22	3	1	2	12	1	14	1	0	4	0	7	4	98	42	0	358	2	0	0	35	1	4	6	6	15	92	15	8	24	31	0	4	10	6	7	29	23	12	9	2	0	1	1	19	0	0	3	1	19	0	4	20	2	20	4	0	1	46	18	0	3	8	3	0	2	2	1	44	4	11	0	3	4	15	2	1	69	36	8	87	6	3	29	1	6	2	5	4	2	0	9	0	3	9	1	21	2	37	2	8	0	41	0	4	15	88	2	5	18	0	14	102	1	0	28	8	1	7	1	0	1	7	3	1	75	4	0	96	0	0	2	3	3	4	11	0	17	0	9	4	50	5	1	0	0	1	29	0	0	4	11	0	11	1	4	5	7	10	1	50	37	2	1	3	5	20	9	7	2	9	1	3	9	10	40	23	0	10	0	1	5	0	2	6	1	4	3	117	1	285	4	13	4	14	2	0	9	9	2	6	34	3	1	2	1	56	64	0	26	1	75	2'
webSciDLVector = getIntFromList(webSciDLVector)

fMeasureVector = '1	4	4	1	3	23	1	9	5	1	3	2	2	17	2	12	4	4	0	0	0	1	27	7	0	1	2	7	15	5	7	19	3	2	61	1	0	2	5	3	3	1	5	7	13	0	13	3	1	1	2	8	5	1	2	0	3	5	2	3	21	4	5	5	3	41	8	2	4	4	23	2	4	7	1	0	1	3	2	3	4	1	0	8	5	0	5	7	9	1	15	7	2	14	8	5	4	4	15	5	50	4	2	0	9	4	2	1	8	4	4	4	3	3	2	1	12	3	7	3	0	4	5	6	3	3	3	5	5	1	5	1	19	25	6	11	14	1	4	6	6	5	2	45	2	7	1	2	3	2	2	5	9	3	3	10	2	2	3	10	2	5	1	11	8	29	5	5	11	3	0	13	4	2	2	4	1	2	3	0	2	18	9	6	1	5	15	7	0	1	2	3	2	8	1	4	1	4	0	2	3	0	4	8	27	5	8	0	3	2	1	8	14	0	2	1	1	4	2	4	0	2	7	8	5	3	1	1	1	2	0	1	1	8	5	10	4	0	0	12	19	4	2	5	7	4	3	1	5	2	0	14	3	5	2	14	6	10	0	3	5	6	0	3	3	27	3	7	12	3	4	12	5	9	2	18	6	1	1	10	1	3	1	4	2	1	1	10	9	6	2	4	0	4	0	9	2	3	7	2	7	5	10	116	4	2	9	0	1	0	1	4	10	2	7	4	3	2	11	3	1	5	2	2	12	4	5	8	3	0	1	10	3	11	7	11	30	1	5	0	1	0	1	0	1	4	3	26	8	5	3	5	0	2	1	18	2	2	7	4	3	2	4	1	3	1	18	5	3	12	2	1	1	1	0	1	2	4	1	1	14	11	1	1	0	2	7	3	2	2	5	5	13	0	2	1	0	5	1	13	0	0	0	4	7	3	3	8	3	2	2	2	8	27	3	3	0	1	3	0	0	3	1	5	15	2	0	1	5	2	5	0	0	3	3	29	3	1	6	6	7	1	2	3	1	18	15	4	0	10	1	2	2	1	6	5	2	3	0	17	0	10	7	0	61	6	1	2	12	13	0	24	2	0	6	0	0	1	2	3	7	0	13	1	2	2	10	1	16	2	3	1	1	5	1	6	1	2	0	8	0	1	6	5	2	6	1	1	1	12	7	1	0	1	3	2	2	10	0	3	0	0	20	7	1	2	4	4	0	0	26	0	1	4	1	3	0	4	1	1	15	0	2	3	0	6	0	4	0	0	3	2	0	6	4	7	0	1	8	6	0	9	1	17	0	3	1	0	7	0	3	7	15	2	5	14	1	5	9	0	16	1	2	9	2	1	1	1	5	2	4	2	11	9	2	2	2	3	5	1	2	0	0	8	1	5	5	0	0	51	0	1	1	3	22	1	0	0	0	1	3	5	2	11	3	2	0	3	0	2	8	10	10	0	4	0	1	2	3	2	1	3	8	1	0	3	3	2	0	12	1	2	5	3	0	6	3	0	1	8	2	0	0	5	0	0	7	0	0	2	0	3	1	1	4	2	1	1	1	0	21	4	23	2	2	0	1	1	1	0	1	9	4	2	1	1	11	10	0	0	11	7	2	0	7	3	3	4	9	11	1	51	1	4	0	4	3	0	7	2	0	3	2	0	1	1	10	0	6	1	5	1	2	0	1	6	3	0	7	8	2	2	2	1	1	2	1	1	1	9	0	2	0	5	10	9	10	2	14	1	1	13	0	1	1	2	2	4	2	20	1	0	0	2	13	1	2	5	1	0	2	1	4	2	1	1	0	2	7	0	1	5	0	0	3	4	3	4	10	13	2	7	3	4	0	0	3	1	1	11	0	2	14	2	2	1	2	4	4	7	0	3	12	0	0	0	12	1	0	4	0	8	0	4	7	1	0	4	2	2	9	0	2	0	4	5	3	2	4	0	2	1	3	1	1	0	7	5	1	0	1	4	0	4	0	0	9	2	0	7	1	0	6	4	7	20	0	1	0	1	7	2	2	5	3	0	4	1	0	2	0	0	2	0	1	0	4	0	1	1	13	0	3	0	0	0	0	0	2	0	2	3	1	0	4	0	1	0	1	0	3	1	3	1	1	0	1	1	4	2	0	2	11	0	1	4	0	0	0	9	0	0	3	3	2	4	2	0	4	6	4	1	1	2	5	3	5	0	1	3	1	4	4	0	0	1	1	3	0	3	3	1	4	0	0	5	2	1	0	1	0	4	0	5	1	0	2	2	8	0	1	3	1	1	0	4	1	4	6	2	4'
fMeasureVector = getIntFromList(fMeasureVector)

blognames, words, data = readfile('./blogMatrix.txt')
vectors = createVectorData(blognames, data)

k = 10
knnestimate(vectors, webSciDLVector, k+1)

