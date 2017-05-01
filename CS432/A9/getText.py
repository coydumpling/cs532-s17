import feedparser
import re
#from BeautifulSoup import BeautifulSoup as Soup

rss_url = "http://afistop100moviesreviewed.blogspot.com/feeds/posts/default?max-results=120"

feed = feedparser.parse(rss_url)
outFile=open('combined.txt','wb')
contents = []
titles = []
count = 0
count2 = 0

for entry in feed.entries:

    if 'content' in entry:
        content = entry.content
    titles.append(entry.title)
    if count2>0:
        contents.append(entry.content)
    count2+=1


subList = contents[:101]
#with open('test.txt','w+') as f:

for content in subList:
    count += 1
    print '\n'
    print count
    parsedTitle = re.sub('\#[0-9]+ ','',titles[count])
    parsedTitle2 = re.sub(r'\([^)]*\)','',parsedTitle)

    #try to parse here
    #print(parsedContent)
    #[{'base': u'http://afistop100moviesreviewed.blogspot.com/feeds/posts/default?max-results=120', 'type': u'text/html', 'value': u'
    #&nbsp;
    #\
    parsedContent = re.sub('<[^>]*>', ' ', str(content))
    parsedContent2 = parsedContent[134:]
    parsedContent3 = re.sub("\\\\",'', parsedContent2)
    parsedContent4 = re.sub("   ",' ', parsedContent3)
    parsedContent5 = re.sub("  ", ' ', parsedContent4)
    parsedContent6 = re.sub('&nbsp;','',parsedContent5)
    parsedContent7 = parsedContent6[:-22]
    parsedContent8 = re.sub('Plot summary \(with spoilers\)\:','',parsedContent7)
    parsedContent9 = re.sub("  ", '', parsedContent8)

    combined = parsedTitle2 + parsedContent9
    combined2 = re.sub('Plot Summary \(with spoilers\)\:','',combined)

    #parsedCombined = re.sub("'","\\'",combined2)
    parsedCombined2 = re.sub('"','',combined2)

    print parsedCombined2
    if(count>0):
        outFile.write(parsedCombined2+'\n')

