# coding: utf-8
import docclass

#open file where categories are stored
outFile = open('ActualCats.txt','r')

#open file containing combinations of both summaries and titles
outFile2 = open('shortenedCombined.txt','r')

titles = []
categories = []
combined = []

#populate lists with files
for entry in outFile:
   categories.append(entry)
for entry in outFile2:
   combined.append(entry)

count = 0

count2 = 0
#change this variable every one to get the values 1 = 0-9; 10 = 90-99
n = 9
#n*10 indicates what cross validation values are in each file. example: n=3 has values 21-30
cVal = "cValidation" + str(n*10)+".txt"
crossVal = open(cVal,"wb")
cl = docclass.fisherclassifier(docclass.getwords)

#clear database file in project after every run to ensure consistency
cl.setdb('cross.db')

#create cross 10 sublists
classified =  combined[((n-1)*10):(n*10)]
sublist2 =  combined[:(n-1)*10]
sublist3 =  combined[(n)*10:]
trainingdata_Entries = sublist2+sublist3

#Categories to be classified
#c =  categories[((n-1)*10):(n*10)]
sublist5 =  categories[:(n-1)*10]
sublist6 =  categories[(n)*10:]
trainingdata_Categories= sublist5+sublist6

while count < 90:
       docclass.choochoo(cl, trainingdata_Entries[count], trainingdata_Categories[count])
       count += 1
count =0

while count2 < 10:
   print count2
   print classified[(count2)]
   prediction = cl.classify(classified[(count2)])
   crossVal.write(prediction)
   count2 += 1

