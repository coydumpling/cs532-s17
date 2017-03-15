library(igraph)

#undirected graph
g <- read.graph("C:/CS432/A5/karate.gml", format="gml")

#find the edge betweenness 
ebc <-edge.betweenness.community(g)

#color corresponds with membership; for 5 clusters
#V(g)$color <- ebc$membership + 5

V(g)$color <- "gray"
V(g)$color[1] <- "blue"
V(g)$color[34] <- "blue"


# for two clusters
# V(g)$color[22] <- "red"
# V(g)$color[20] <- "red"
# V(g)$color[8] <- "red"
# V(g)$color[2] <- "red"
# V(g)$color[4] <- "red"
# V(g)$color[11] <- "red"
# V(g)$color[14] <- "red"
# V(g)$color[13] <- "red"
# V(g)$color[18] <- "red"
# V(g)$color[12] <- "red"
# V(g)$color[5] <- "red"
# V(g)$color[6] <- "red"
# V(g)$color[7] <- "red"
# V(g)$color[17] <- "red"

# for three clusters
# V(g)$color[10] <- "purple"
# 
# V(g)$color[2] <- "red"
# V(g)$color[4] <- "red"
# V(g)$color[5:8] <- "red"
# V(g)$color[11:14] <- "red"
# V(g)$color[17:18] <- "red"
# V(g)$color[20] <- "red"
# V(g)$color[22] <- "red"

# for three clusters
V(g)$color[10] <- "purple"

V(g)$color[2] <- "red"
V(g)$color[4] <- "red"
V(g)$color[8] <- "red"
V(g)$color[12:14] <- "red"
V(g)$color[18] <- "red"
V(g)$color[20] <- "red"
V(g)$color[22] <- "red"

V(g)$color[5:7] <- "green"
V(g)$color[11] <- "green"
V(g)$color[17] <- "green"




#plot(g,  layout = layout.fruchterman.reingold, vertex.label.color = "cyan", vertex.size = 15)


#delete edges to find the remaining components that make up the communities
mods <- sapply(
0:ecount(g), function(i){ 
g2 <- delete.edges(g, ebc$removed.edges[seq(length=i)]) 
cl <- clusters(g2)$membership
if(no.clusters(g2)==4){
    plot(g2, layout = layout.fruchterman.reingold, vertex.label.color = "white", vertex.size = 15)
    }
  }
)
