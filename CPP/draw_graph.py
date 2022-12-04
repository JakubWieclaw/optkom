import networkx as nx
import matplotlib.pyplot as plt

with open ("mycie14.txt", "r") as f:
    lines = f.readlines()

lines = lines[1:]
g = nx.Graph()
for l in lines:
    v, u = l.split()
    v = int(v) -1
    u = int(u) -1
    g.add_edge(v,u)
print(nx.algorithms.approximation.max_clique(g))
nx.draw(g, with_labels = True)
plt.show()
