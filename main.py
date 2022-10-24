from Graph import Graph
from algorithms import execute_and_measure_time, greedy_graph_coloring


g = Graph()
g.generate_random_simple_graph(100, 0.5)
# g.create_graph_from_dr_machowiaks_file("test_instance.txt")
# g.draw()
colors = execute_and_measure_time(greedy_graph_coloring, 1000, g)
g.draw(colors=colors)