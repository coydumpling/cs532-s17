import requests

f = open('urls.txt', 'w')
s = set()
while (len(s) < 100):
    url = "http://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117"
    r = requests.get(url)
    r.status_code == requests.codes.ok
    print('good link #') + str(r.status_code)
    update = r.url.strip('/?expref=next-blog')+('/feeds/posts/default?alt=rss'+'\n')
    s.add(update)
for element in s:
    print element
    f.write(element + '\n')
f.write('http://f-measure.blogspot.com' + '\n' + '\n')
f.write('http://ws-dl.blogspot.com')
