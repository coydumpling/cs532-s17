import feedparser
import re

rss_url = "http://afistop100moviesreviewed.blogspot.com/feeds/posts/default?max-results=120"

feed = feedparser.parse(rss_url)

with open('titles.txt', 'w+') as f:
    for post in feed.entries:
        parsedTitle = re.sub('\#','', post.title)
        parsedTitle2 = re.sub(r'\([^)]*\)', '', parsedTitle)
        parsedTitle3 = re.sub(r'[0-9]+ ', '', parsedTitle2)
        print parsedTitle3 + "\n"
        f.write(parsedTitle3 + "\n")

