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

from MatrixGraph import MatrixGraph
from algorithms import greedy_graph_coloring

graph = MatrixGraph(0, "CPP/mycie14.txt")
size_of_tabu_list = 7
number_of_neighbours = 10
number_of_iterations = 1000

print(greedy_graph_coloring(graph))
print(graph)
