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

graph = MatrixGraph(0, "../instances/gc500.txt")
# graph = MatrixGraph(0, "instances/test_instance.txt")
# s = greedy_graph_coloring(graph)
# k = len(s)
k = 86
print(f"Greedy coloring number: {k}")
# rc = random_coloring(graph, k)
# print(rc)
while True:
    rc = random_coloring(graph, k-1)
    new_solution = tabu_search(graph, len(rc), rc, size_of_tabu_list=7, number_of_neighbours=50, max_number_of_iterations=20000)
    if new_solution is None:
        break
    else:
        s = new_solution
        k = len(s)
        print(k)

print("Final solution: ", len(s))