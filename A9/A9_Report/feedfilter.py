import feedparser
import re
import os, sys


def getClassData(feed, classifier, inputFilename, mode, maxItemsToTestOrTrain, 
wordOrEntry='word'):

  if( len(feed) > 0 and len(inputFilename) > 0 and (mode == 'train' or mode == 'test') 
  and maxItemsToTestOrTrain > 0 and (wordOrEntry == 'word' or wordOrEntry == 'entry')):

    #inputFilename: <title, titleText, classLabel>
    try:
      inputFile = open(inputFilename, 'r')

      if( mode == 'test' ):
        prefix = inputFilename.split('.')[0]
        outputFile = open(prefix+'Predictions.txt', 'w')

      lines = inputFile.readlines()
      inputFile.close()
      #first line is schema
      del lines[0]
      print( len(lines), 'lines read from ' + inputFilename)
    except:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print((fname, exc_tb.tb_lineno, sys.exc_info() ))
      return

    if( mode == 'test' ):
      outputFile.write('TITLE <> PROB <> PREDICTED-LABEL <> ACTUAL-LABEL\n')

    # Get feed entries and loop over them
    f=feedparser.parse(feed)
    count = 1
    for entry in f['entries']:

      for l in lines:

        titleContentLabel = l.split('<>')

        title = titleContentLabel[0].strip()
        #print('\ttitle:', title)
        summary = titleContentLabel[1].strip()
        actualClassLabel = titleContentLabel[2].strip()

        if( title.lower() == entry['title'].strip().lower() ):
          fulltext='%s\n%s' % (entry['title'],entry['summary'])

          if( mode == 'train' ):
            #training get the correct category and train on that

            if( wordOrEntry == 'word' ):
              classifier.train(fulltext, actualClassLabel)
            else:
              classifier.train(entry, actualClassLabel) 

            print( '...training count:', count)
          else:
            #testing: guess the best guess at the current category
            try:
              if( wordOrEntry == 'word' ):
                prediction = str(classifier.classify(fulltext))
              else:
                prediction = str(classifier.classify(entry))

              classPredictionProbability = classifier.getGlobalCProbValue()
              print( '...testing count', count)
              print( title + ' <> ' + str(classPredictionProbability) + ' <> ' 
              + prediction + ' <> ' + actualClassLabel )
              outputFile.write(title + ' <> ' + str(classPredictionProbability) + ' <> ' 
              + prediction + ' <> ' + actualClassLabel + '\n')
            except:
              exc_type, exc_obj, exc_tb = sys.exc_info()
              fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
              print((fname, exc_tb.tb_lineno, sys.exc_info() ))
              print( '...skipping', count)
              
            

          if(count == maxItemsToTestOrTrain):
            print( '...max items reached, closing')

            if( mode == 'test' ):
              outputFile.close()

            return

          count += 1

    if( mode == 'test' ):
      outputFile.close()