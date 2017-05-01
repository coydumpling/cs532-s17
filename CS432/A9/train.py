# coding: utf-8
import docclass

#open file where categories are stored
categories=open('ActualCats.txt','r')

#open file containing combinations of both summaries and titles
shortCombo= open('shortenedCombined.txt','r')

count=0
titles=[]
#categories
cats=[]
#predictions
preds=[]
#summaries and titles
combined=[]
#training data set to 50 and 90
tCount50=50
tCount90=90
#maximum training data
maxData=100

#populate lists with files
for entry in categories:
   cats.append(entry)
for entry in shortCombo:
   combined.append(entry)

cl=docclass.fisherclassifier(docclass.getwords)

#clear database file in project after every run to ensure consistency
cl.setdb('mmg.db')

#train the first entries in the title summary text file
for entry in combined:
    #comment and uncomment as needed; used for Q3
   if count < tCount50:
   #if count<tCount90:
      docclass.choochoo(cl,entry,cats[count])
      count += 1

w = maxData - count
intialpreds = maxData - count

# classify the remaining entries
while count < maxData:
   print count
   pred = cl.classify(combined[(count)])
   preds.append(pred)
   count += 1

if len(preds) > 49:
    #open file where categories are stored
    CFifty = open('Classify50.txt','w')
    
if len(preds) < 11:
    #open file containing combinations of both summaries and titles
    CTen = open('Classify10.txt','w')

print(len(preds))

for pred in preds:
    if len(preds)>49:

        CFifty.write(pred)
        
    if len(preds)<11:

        CTen.write(pred)
