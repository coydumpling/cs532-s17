import re

parsedCombined2 = open('combined.txt','r')
outfile = open('shortenedCombined.txt','w+')

for line in parsedCombined2:
    s = ''.join(sentence + '.' for sentence in re.split('\.(?=\s*(?:[A-Z]|$))', line, maxsplit=7)[:-1])
    print s
    outfile.write(s+"\n")

