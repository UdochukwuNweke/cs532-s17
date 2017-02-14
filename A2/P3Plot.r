ageData <-  read.csv('./agePlotData.csv', head=TRUE, sep=",")
plot(ageData$Age, ageData$MementoCount, log='xy', main='Age vs. Number of mementos', xlab='Age (days)', ylab='Number of mementos')