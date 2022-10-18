from Graph import Graph
from algorithms import greedy_graph_coloring

g = Graph()
g.generate_random_simple_graph(10, 0.5)
g.create_graph_from_dr_machowiaks_file("test_instance.txt")
# g.draw()
g.draw(colors=greedy_graph_coloring(g))