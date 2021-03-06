

g=read.graph('/Users/mgrah/mln.graphml',format='graphml')


df <- get.data.frame(g, what='vertices')
df$id <- as.numeric(gsub("[A-Za-z]+", "", df$id)) #if you need only the `numeric` part
row.names(df) <- NULL
df1 <- df[,c(1,15,16)]
df1

df2 <-df[15]

#x=read.table('/Users/mgrah/friend_count.txt')

col <- c(rep(c("purple"),42),rep(c("pink"),1),rep(c("purple"),111))

barplot(height = c(7, 15, 25, 30, 38, 39, 40, 41, 41, 42, 43, 54, 58, 59, 60, 62, 65, 68, 68, 77, 80, 85, 86, 87, 89, 93, 94, 94, 96, 97, 104, 104, 106, 108, 111, 123, 124, 128, 131, 143, 144, 147, 154, 155, 165, 168, 168, 170, 172, 181, 182, 183, 186, 187, 190, 195, 197, 204, 207, 208, 220, 227, 229, 231, 231, 233, 233, 235, 236, 240, 241, 242, 244, 245, 245, 250, 255, 259, 274, 275, 276, 278, 295, 297, 297, 308, 312, 315, 317, 321, 321, 322, 324, 327, 328, 337, 348, 351, 353, 359, 363, 366, 380, 387, 400, 404, 409, 415, 420, 421, 424, 425, 425, 427, 436, 443, 448, 449, 458, 496, 510, 524, 528, 538, 539, 552, 555, 555, 561, 562, 568, 575, 576, 580, 592, 615, 619, 622, 624, 705, 752, 763, 770, 784, 819, 833, 844, 873, 909, 1194, 1346, 1512, 1521, 1626, 3187), col=col, border='cyan',main="Facebook Friendship: MLN",xlab="Sorted in Increase",ylab="Friend Count")