

histData <-  read.csv('./MementoCounts.csv', head=TRUE, sep=",")
hist(histData$MementoCount, xlab='Number of Mementos', ylab='Frequency of Occurence', main='Number of Mements vs. Frequency of Occurence')