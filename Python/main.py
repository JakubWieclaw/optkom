"""it is possible that class Graph is not working properly"""
"""i suspect that after analyse adjecancy_matrix from to_adjecancy_matrix() method"""
"""if need be to check / fix"""
# from Graph import Graph
# from algorithms import execute_and_measure_time, greedy_graph_coloring
# g = Graph()
# wierzcholków 100 i 20
# g.generate_random_simple_graph(15, 0.3)
# g.create_graph_from_dr_machowiaks_file("test_instance.txt")
# g.draw()
# colors = execute_and_measure_time(greedy_graph_coloring, 1, g, True)
# colors = greedy_graph_coloring(g)
# print(colors)
# print("Number of colors: ", len(set(colors.values())))
# g.draw(colors=colors)

import random

from MatrixGraph import MatrixGraph
from algorithms import greedy_graph_coloring
from tabusearch import f, tabu_search

def random_coloring(graph, k):
    coloring = []
    for _ in range(k):
        coloring.append(list())
    for node in graph.nodes():
        coloring[random.randint(0, k-1)].append(node)
    return coloring

# graph = MatrixGraph(0, "CPP/mycie14.txt")
graph = MatrixGraph(0, "test_instance.txt")
s = greedy_graph_coloring(graph)
k = len(s)

print(random_coloring(graph, k))
print(graph)

print(tabu_search(graph, k, random_coloring(graph, k), size_of_tabu_list=7, number_of_neighbours=1000, max_number_of_iterations=10000))
