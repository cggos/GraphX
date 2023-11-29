import igraph as ig

g1 = ig.Graph.GRG(100, 0.2)
g2 = ig.Graph.GRG(100, 0.2)

g1["date"] = "2023-11-29"
print(g1["date"])

ig.summary(g1)

print(g1.get_edgelist() == g2.get_edgelist())

print(g1.isomorphic(g2))

ig.plot(g1)
