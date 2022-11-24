from Graph import Graph
from algorithms import execute_and_measure_time, greedy_graph_coloring, sort_nodes_by_reduction
import networkx as nx

g = Graph()
# wierzcholków 100 i 20
g.generate_random_simple_graph(15, 0.3)
print(sort_nodes_by_reduction(g))
print(nx.coloring.strategy_smallest_last(g, None))
# g.create_graph_from_dr_machowiaks_file("test_instance.txt")
# g.draw()
# colors = execute_and_measure_time(greedy_graph_coloring, 1, g, True)
# colors = greedy_graph_coloring(g)
# print(colors)
# print("Number of colors: ", len(set(colors.values())))
# g.draw(colors=colors)