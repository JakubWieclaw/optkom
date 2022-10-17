from tkinter import N
from Graph import Graph
from algorithms import greedy_graph_coloring

g = Graph()
g.generate_random_simple_graph(20, 0.5)
print(greedy_graph_coloring(g))