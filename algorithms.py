from Graph import Graph
import networkx as nx

def greedy_graph_coloring(graph : Graph) -> dict:
    """Greedy graph coloring algorithm"""
    # TODO: Implement your own greedy graph coloring algorithm
    return nx.greedy_color(graph)