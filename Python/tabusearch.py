import random
from copy import deepcopy

class Conflict:
    def __init__(self, vertice : set, color : int):
        self.vertice = vertice
        self.color = color
    def __str__(self):
        return f"Conflict: {self.vertice} {self.color}"

def f(graph, solution, conflicts=None):
    res = 0
    if conflicts is None:
        for l in solution:
            for v in l:
                for w in l:
                    if v > w and graph.is_edge(v, w):
                        res += 1
    else:
        for i in range(len(solution)):
            for v in solution[i]:
                for w in solution[i]:
                    if v > w and graph.is_edge(v, w):
                        conflicts.append(Conflict({v, w}, i))
                        res += 1
    return res

def tabu_search(graph, k, s, size_of_tabu_list=7, number_of_neighbours=10, max_number_of_iterations=1000):
    number_of_iterations = 0
    T = []

    while f(graph, s) and number_of_iterations < max_number_of_iterations:
        number_of_iterations += 1
        neighbours = []
        bestFound = False
        if len(T) == size_of_tabu_list:
            T.pop(0)

        for _ in range(number_of_neighbours):
            neighbours.append(deepcopy(s))

        # TODO: vertex should be drawn from those that are in conflict
        moves = [] # list of tuples (vertex, color)
        conflicts = []
        f_graph_s = f(graph, s, conflicts)
        # print(f"len(conflicts): {len(conflicts)}")
        # print(f"conflicts: {conflicts}")
        for neighbour in neighbours: # generate neighbours
            random_conflict = random.choice(conflicts)
            random_vertex = random.choice(list(random_conflict.vertice))
            idx_k_from = random_conflict.color
            idx_k_to = random.randint(0, k-2)
            if idx_k_to == idx_k_from:
                idx_k_to = k-1

            neighbour[idx_k_from].remove(random_vertex)
            neighbour[idx_k_to].append(random_vertex)

            moves.append((random_vertex, idx_k_to))

            if moves[-1] not in T and f(graph, neighbour) < f_graph_s:  # if better solution found, stop generating neighbours
                s = neighbour
                T.append(moves[-1])
                bestFound = True
                break

        if not bestFound:
            minF = float('inf')
            minIdx = None
            for i in range(len(neighbours)):
                if moves[i] not in T and f(graph, neighbours[i]) < minF:
                    minIdx = i
                    minF = f(graph, neighbours[i])
            if minIdx is None:
                print("All possible moves are in tabu list")
                minIdx = 0
            s = neighbours[minIdx]
            T.append(moves[minIdx])

        moves.clear()

    if f(graph, s) == 0:
        return s
    return None
