import igraph as ig

g = ig.Graph([(0, 1), (0, 2), (2, 3), (3, 4), (4, 2), (2, 5), (5, 0), (6, 3), (5, 6)])

g.vs["name"] = ["Alice", "Bob", "Claire", "Dennis", "Esther", "Frank", "George"]
g.vs["age"] = [25, 31, 18, 47, 22, 23, 50]
g.vs["gender"] = ["f", "m", "f", "m", "f", "m", "m"]
g.es["is_formal"] = [False, False, True, True, True, False, True, False, False]

print(g.get_adjacency())

g.vs["label"] = g.vs["name"]
color_dict = {"m": "blue", "f": "pink"}
g.vs["color"] = [color_dict[gender] for gender in g.vs["gender"]]

layout = g.layout("kk")

if 0:
    ig.plot(g, layout=layout, bbox=(300, 300), margin=20)
else:
    visual_style = {}
    visual_style["vertex_color"] = [color_dict[gender] for gender in g.vs["gender"]]
    visual_style["vertex_size"] = 20
    visual_style["vertex_label"] = g.vs["name"]
    visual_style["edge_width"] = [1 + 2 * int(is_formal) for is_formal in g.es["is_formal"]]
    visual_style["layout"] = layout
    visual_style["bbox"] = (300, 300)
    visual_style["margin"] = 20
    ig.plot(g, **visual_style)
