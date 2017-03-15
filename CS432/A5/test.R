library(igraphdata)
data(karate)
karate <- karate %>%
  add_layout_(with_fr()) %>%
  set_vertex_attr("size", value = 10)

cl_k <- cluster_optimal(karate)

V(karate)$color <- membership(cl_k)
karate$palette <- categorical_pal(length(cl_k))
plot(karate)
