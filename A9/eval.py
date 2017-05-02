import os, sys

from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

def getPredictActualLabels(inputFileName):

	listOfPredictedLabels = []
	listOfActualLabels = []

	try:
		inputFile = open(inputFileName, 'r')
		lines = inputFile.readlines()
	
		del lines[0]
		print( len(lines), 'lines read from ' + inputFileName )
		inputFile.close()
	except:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		print(fname, exc_tb.tb_lineno, sys.exc_info() )

	for l in lines:

		predictedAndActualLabel = l.split(' <> ')
		if( len(predictedAndActualLabel) > 1 ):

			predictedAndActualLabel = predictedAndActualLabel[-2:]

			predictedLabel = predictedAndActualLabel[0].strip()
			actualLabel = predictedAndActualLabel[1].strip()

			listOfPredictedLabels.append(predictedLabel)
			listOfActualLabels.append(actualLabel)

	return listOfPredictedLabels, listOfActualLabels

def main(predictionFilename):

	infile = open('./predictionLabels.txt', 'r')
	labels = infile.read()
	infile.close()

	labels = labels.split(', ')
	print('\tlabels:', labels)

	listOfPredictedLabels, listOfActualLabels = getPredictActualLabels(predictionFilename)

	confusionMatrix = confusion_matrix( listOfActualLabels, listOfPredictedLabels, labels=labels )
	precision = precision_score( listOfActualLabels, listOfPredictedLabels, labels=labels, average='macro' )
	recall = recall_score( listOfActualLabels, listOfPredictedLabels, labels=labels, average='macro' )
	f1 = f1_score( listOfActualLabels, listOfPredictedLabels, labels=labels, average='macro' )

	print('\nconfusion matrix:')
	print( confusionMatrix )

	print('\nprecision:')
	print( precision )

	print( '\nrecall:' )
	print( recall )

	print( '\nf1' )
	print( f1 )

if __name__ == "__main__":

	if( len(sys.argv) != 2 ):
		print('\tMissing prediction input filename')
		print('\tE.g python eval.py Testing-50Predictions.txt')
	else:
		main( sys.argv[1] )

