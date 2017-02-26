# encoding=utf8
from bs4 import BeautifulSoup
from newspaper import Article
import urllib
import requests
import sys

reload(sys)
sys.setdefaultencoding('utf8')

count = 1

with open('urls.txt', 'r') as f: #text file containing the URLS


    for url in f:
        if url.strip() != "":
            pFile = 'processed_'+str(count)+'.txt'
            rFile = 'raw_'+str(count)+'.txt'

            with open(rFile, 'a') as fout:
                print(u"URL Line: {}".format(url.encode('utf-8')))

                # you might want to remove endlines and whitespaces from
                # around the URL, which what strip() does
                article = Article(url.strip())
                article.download()
                article.parse()

                # write/append to file
                fout.write(article.html)
                print(u"Raw HTML: {}".format(article.html.encode('utf-8')))

            with open(pFile,'a') as fout:
                print(u"URL Line: {}".format(url.encode('utf-8')))

                # you might want to remove endlines and whitespaces from
                # around the URL, which what strip() does
                article = Article(url.strip())
                article.download()
                article.parse()

                # write/append to file

                fout.write(article.title)
                fout.write(article.text)

                print(u"Title: {}".format(article.title.encode('utf-8')))

                # print authors only if there are authors to show.
                if len(article.authors) == 0:
                    print('No author!')
                else:
                    for author in article.authors:
                        print(u"Author: {}".format(author.encode('utf-8')))

                print("Text of the article:")
                print(article.text.encode('utf-8'))
                count+=1
