import clusters
import sys
import codecs

blognames, words, data = clusters.readfile('blogdata1.txt')

clust = clusters.hcluster(data)

with codecs.open('ascii', 'w+', encoding ="ascii") as fout:
    clusters.printclust(clust, labels=blognames)

clusters.drawdendrogram(clust, blognames, jpeg='dendrogram.jpg')
