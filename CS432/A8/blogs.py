import requests
from collections import Counter
s = set()
counter = Counter()
while (len(s) < 5):
    url = "http://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117"
    r = requests.get(url)
    if (r.status_code == requests.codes.ok):
        counter += Counter(s)
        print('Status Code: ') + str(r.status_code) + str(counter)
with open("urls.txt", "w+") as fout:
    for element in s:
        print element
        f.write(element + '\n')
f.write(uri.strip('/?expref=next-blog')+'/feeds/posts/default?alt=rss'+'\n')
f.write('http://f-measure.blogspot.com' + '\n')
f.write('http://ws-dl.blogspot.com')
