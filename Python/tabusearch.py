# from queue import Queue
import random
from copy import deepcopy

def f(graph, solution):
    res = 0
    for l in solution:
        for v in l:
            for w in l:
                if graph.is_edge(v, w):
                    res += 1
    return res

def tabu_search(graph, k, s, size_of_tabu_list=7, number_of_neighbours=10, max_number_of_iterations=1000):
    number_of_iterations = 0
    T = []

    while f(graph, s) and number_of_iterations < max_number_of_iterations:
        # print(f(graph, s))
        # print()
        number_of_iterations += 1
        neighbours = []
        bestFound = False
        if len(T) == size_of_tabu_list:
            T.pop(0)

        for _ in range(number_of_neighbours):
            neighbours.append(deepcopy(s))

        # TODO: check if there are empty lists in neighbour (didn't use color)
        for neighbour in neighbours:
            moves = []
            while True:
                idxs_k_to_choose = [i for i in range(k)]
                while True:
                    idx_k_from = random.choice(idxs_k_to_choose)
                    if len(neighbour[idx_k_from]) > 0:
                        break
                idxs_k_to_choose.remove(idx_k_from)
                idx_k_to = random.choice(idxs_k_to_choose)
                random_vertex = random.choice(neighbour[idx_k_from])

                neighbour[idx_k_from].remove(random_vertex)
                neighbour[idx_k_to].append(random_vertex)

                moves.append((random_vertex, idx_k_from))

                if f(graph, neighbour) < f(graph, s):
                    s = neighbour
                    T.append(moves[-1])
                    bestFound = True
                    break

        if not bestFound:
            minF = float('inf')
            minIdx = None
            for i in range(len(neighbours)):
                if f(graph, neighbours[i]) < minF:
                    minIdx = i
                    minF = f(graph, neighbours[i])
                    break
            s = neighbours[minIdx]
            T.append(moves[minIdx]) # TODO: list index out of range - once error appeared

        number_of_iterations += 1

    if f(graph, s) == 0:
        return s
    return None