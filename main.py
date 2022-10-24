from Graph import Graph
from algorithms import execute_and_measure_time, greedy_graph_coloring


g = Graph()
# wierzcholków 100 i 20
# g.generate_random_simple_graph(15, 0.3)
# g.save_to_txt_file("xd.txt")
# g.create_graph_from_dr_machowiaks_file("xd.txt")
# g.create_graph_from_dr_machowiaks_file("dane2.txt")
g.create_graph_from_dr_machowiaks_file("file2.txt")
# g.draw()
# colors = execute_and_measure_time(greedy_graph_coloring, 1, g, True)
colors = greedy_graph_coloring(g)
print(colors)
print("Number of colors: ", len(set(colors.values())))
g.draw(colors=colors)