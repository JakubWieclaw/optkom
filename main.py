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

graph = MatrixGraph(0, "test_instance.txt")
