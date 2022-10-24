from Graph import Graph
import networkx as nx
from time import time

def sort_nodes_by_reduction(graph : Graph) -> list:
    """Sorts nodes by reduction. The node removed as first (the least degree) is last in the list"""
    sorted_nodes = list()
    graph_copy = graph.copy()
    while (graph_copy.number_of_nodes() > 0):
        tmp_max_node = min(graph_copy.nodes, key=lambda node: graph_copy.degree[node])
        sorted_nodes.append(tmp_max_node)
        graph_copy.remove_node(tmp_max_node)
    sorted_nodes.reverse()
    return sorted_nodes

def greedy_graph_coloring(graph : Graph, use_builtin_algorithm=False) -> dict:
    """Greedy graph coloring SL algorithm"""
    if not use_builtin_algorithm:
        colors = set(range(0, graph.number_of_nodes())) # colors are just numbers, generated from 0 to number of nodes-1 (maximal number of colors)
        coloring = dict()
        for node in sort_nodes_by_reduction(graph): # for each node in proper order
            possible_colors_to_use = colors.copy()
            for neighbor in graph.neighbors(node): # for each neighbor of the node
                if neighbor in coloring: # if the neighbor is already colored
                    possible_colors_to_use.discard(coloring[neighbor]) # remove the color of the neighbor from possible colors to use
            coloring[node] = min(possible_colors_to_use) # color the node with the 'lowest' possible color (number)
        return coloring
    else: # use builtin algorithm
        print("Using builtin algorithm")
        return nx.greedy_color(graph, strategy="smallest_last")

def execute_and_measure_time(func, avg_by : int, *args, **kwargs):
    """Executes function and measures time. Return object returned by func"""
    avg = 0
    ret = None
    for i in range(avg_by):
        start = time()
        ret = func(*args, **kwargs)
        end = time()
        avg += (end - start)
    avg /= avg_by
    print("Time: ", avg)
    return ret