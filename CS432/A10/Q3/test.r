histData <- read.table("C:/CS432/A10/Q3/differenceTimeMaps")
hist(histData$V1, xlab='Number of Mementos', xlim = range(c(-10,10)), 
     ylab='Frequency of Occurence', main='Mementos vs. Frequency', 
     ty =4, col ='pink', border = 'red')

oldData <- read.table("C:/CS432/A10/Q3/finalMementoList10")
hist(histData$V1, xlab='Number of Mementos',
     ylab='Frequency of Occurence', main='Mementos vs. Frequency', 
     ty =4, col ='cyan', border = 'blue')

