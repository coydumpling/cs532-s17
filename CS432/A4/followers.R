import igraph

read.table('C:/CS432/A4/TwitterFollowers.txt')

barplot(height = c(15, 31, 42, 45, 69, 80, 91, 113, 135, 178, 199, 214, 289, 305, 414, 437, 534, 556, 620, 908, 1011, 1021, 1273, 1820, 1917, 2003, 3122, 3323, 3408, 3441, 4545, 6611, 8716, 10797, 13886, 14429, 15408, 18008, 19336, 21775, 25519, 27388, 79011, 100807, 126108, 140128, 140335, 179489, 246560, 310115, 406148), col="purple", border='cyan',main="Twitter Friendship: Me",xlab="Sorted in Increase",ylab="Followers Count")