library(tidyverse)
library(tidygraph)
library(igraph)
library(ggraph)

set.seed(1236)



g <- play_geometry(200, .15, torus = FALSE)

# g <- play_barabasi_albert(300, 0.5, 10)

viz <- g %>% 
  ggraph(layout = 'kk') + 
  geom_edge_link(alpha = 0.3) + 
  geom_node_point(size = 4, pch = 21, fill = "#73b9ee") + 
  theme_void() + 
  scale_edge_width_manual(values = c(.3, 2)) +  
  guides(edge_color = "none", edge_width = "none")


ggsave("assets/img/network-toy-viz.png", viz, width = 12, height = 9, dpi = 300) 
 