autos_data <- read.table("C:/CS432/A10/Q3/differenceTimeMaps")
plot(autos_data$V1, type="l", col="blue", xlab ="URI Listing",ylab="Change in Timemaps", col.lab=rgb(0,0.5,0), ylim=c(-10,10))
title(main ="Difference in timemaps bewteen Assignment 2 and 10", col.main= "red", font.main = 4)
