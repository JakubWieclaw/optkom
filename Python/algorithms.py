# from Graph import Graph
# import networkx as nx
# from time import time
from copy import deepcopy
from MatrixGraph import MatrixGraph

def sort_nodes_by_reduction(graph : MatrixGraph) -> list:
    """Sorts nodes by reduction. The node removed as first (the least degree) is last in the list"""
    sorted_nodes = list()
    graph_copy = deepcopy(graph)
    while (graph_copy.number_of_nodes() > 0):
        tmp_min_node = graph_copy.get_node_with_min_degree()
        sorted_nodes.append(tmp_min_node)
        graph_copy.remove_node(tmp_min_node)
    sorted_nodes.reverse()
    return sorted_nodes
#     else:
#         print("Using builtin algorithm for sorting nodes")
#         return nx.coloring.strategy_largest_first(graph) # results are different than implemented above algorithm

def greedy_graph_coloring(graph : MatrixGraph) -> list:
    """Greedy graph coloring SL algorithm"""
    colors = set(range(0, graph.number_of_nodes())) # colors are just numbers, generated from 0 to number of nodes-1 (maximal number of colors)
    coloring = dict()
    for node in sort_nodes_by_reduction(graph): # for each node in proper order
        possible_colors_to_use = colors.copy()
        for neighbor in graph.successors(node): # for each neighbor of the node
            if neighbor in coloring: # if the neighbor is already colored
                possible_colors_to_use.discard(coloring[neighbor]) # remove the color of the neighbor from possible colors to use
        coloring[node] = min(possible_colors_to_use) # color the node with the 'lowest' possible color (number)
    used_colors = set(coloring.values())
    coloring_list = []
    for _ in used_colors:
        coloring_list.append(list())
    for node, color in coloring.items():
        coloring_list[color].append(node)
    return coloring_list
#     else: # use builtin algorithm
#         print("Using builtin algorithm")
#         return nx.greedy_color(graph, strategy="smallest_last")

# def execute_and_measure_time(func, avg_by : int, *args, **kwargs):
#     """Executes function and measures time. Return object returned by func"""
#     avg = 0
#     ret = None
#     for i in range(avg_by):
#         start = time()
#         ret = func(*args, **kwargs)
#         end = time()
#         avg += (end - start)
#     avg /= avg_by
#     print("Time: ", avg)
#     return ret