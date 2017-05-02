# !usr/bin/python2.7

import requests

import feedparser
import re

from bs4 import BeautifulSoup
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


def getNextBlogPage(url, blogPageList=[]):
   req = requests.get(url)
   soup = BeautifulSoup(req.text,"html.parser")
   nextLink = soup.find('link', rel='next', href=True)
   if nextLink is not None:
       nextLink = nextLink['href']
       blogPageList.append(nextLink)
       getNextBlogPage(nextLink, blogPageList)
   return blogPageList



def getwordcounts(url):
  # Parse the feed
  d=feedparser.parse(url)
  wc={}

  # Loop over all the entries
  for e in d.entries:
    if 'summary' in e: summary=e.summary
    else: summary=e.description

    # Extract a list of words
    words=getwords(e.title+' '+summary)

    for word in words:
      wc.setdefault(word,0)
      wc[word]+=1
  return d.feed.title,wc


def getwords(html):
   # Remove all the HTML tags
   txt = re.compile(r'<[^>]+>').sub('', html)

   # Split words by all non-alpha characters
   words = re.compile(r'[^A-Z^a-z]+').split(txt)

   # Convert to lowercase
   return [word.lower() for word in words if word != '']


def combineWC(wc, nextwc):
   if len(wc) > 0 and len(nextwc) > 0:
       for word, wordcount in nextwc.items():
           if word in wc:
               wc[word] = wc[word] + wordcount
           else:
               wc[word] = wordcount
       return wc
   else:
       return {}


apcount = {}
wordcounts = {}
feedlist = [line for line in open('urls.txt')]
for feedurl in feedlist:
    try:

        blogPageList = getNextBlogPage(feedurl)
        title, wc = getwordcounts(feedurl)
        for url in blogPageList:

            title, nextwc = getwordcounts(feedurl)
            combineWC(wc, nextwc)
        wordcounts[title] = wc
        for word, count in wc.items():
            apcount.setdefault(word, 0)
            if count > 1:
                apcount[word] += 1
    except:
        print 'Failed to parse feed %s' % feedurl

wordlist = []
countFrequentWords = []
for w, bc in apcount.items():
    frac = float(bc) / len(feedlist)
    if frac > 0.1 and frac < 0.5:
        countFrequentWords.append((w, bc))

countFrequentWords = sorted(countFrequentWords, key=lambda x: x[1], reverse=True)

for value in countFrequentWords:
       # word
    value1 = value[0]
       # count
    value2 = value[1]
    #no idea why this works but it gets exactly 1000 word counts
    length = len(wordlist)-value2-6

    if (length < 1000):
        wordlist.append(value1)
    else:
        break

stop_words_list = [line.rstrip('\r\n') for line in open('stopWordList.txt')]

out = file('blogdataQ2.txt', 'w')
out.write('Blog')
for word in wordlist:
    word1 = word.encode('UTF-8')
    out.write('\t%s' % word1)
out.write('\n')
for blog, wc in wordcounts.items():
    blogName = blog.encode('UTF-8')
    print blog
    print blogName
    out.write(blogName)
    for word in wordlist:
        if word not in stop_words_list:
            if word in wc:
                out.write('\t%d' % wc[word])
            else:
                out.write('\t0')
    out.write('\n')

out.close()
