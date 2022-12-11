import random
from copy import deepcopy
import MatrixGraph

class Conflict:
    def __init__(self, vertice : set, color : int):
        self.vertice = vertice
        self.color = color
    def __str__(self):
        return f"Conflict: {self.vertice} {self.color}"

def f(graph : MatrixGraph, solution : list, conflicts : list=None):
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

def tabu_search(graph : MatrixGraph, k : int, s : list, size_of_tabu_list : int=7, number_of_neighbours : int=10, max_number_of_iterations : int=1000):
    number_of_iterations = 0
    T = []
    A = {}

    while f(graph, s) and number_of_iterations < max_number_of_iterations:
        number_of_iterations += 1
        neighbours = []
        f_graph_neighbours = []
        bestFound = False

        # remove first element from tabu list if it's full
        if len(T) == size_of_tabu_list:
            T.pop(0)

        # initialize neighbours (same as s)
        for _ in range(number_of_neighbours):
            neighbours.append(deepcopy(s))

        moves = [] # list of tuples (vertex, color)
        conflicts = []
        f_graph_s = f(graph, s, conflicts)

        # generate neighbours
        """
            neighbours are generated in totally random way
            it means that move done in neighbour could be in tabu list
            is it ok?

            if only neighbours with permitted moves are generated
            would algorithm return better solution?
            would algorithm be more time consuming?
            whether algorithm could fall into infinite loop?
        """
        for neighbour in neighbours:
            # choose random vertex from conflitcs and move it to random color
            random_conflict = random.choice(conflicts)
            random_vertex = random.choice(list(random_conflict.vertice))
            idx_k_from = random_conflict.color
            idx_k_to = random.randint(0, k-2)
            if idx_k_to == idx_k_from:
                idx_k_to = k-1

            neighbour[idx_k_from].remove(random_vertex)
            neighbour[idx_k_to].append(random_vertex)

            # add above move to list of moves
            moves.append((random_vertex, idx_k_to))

            f_graph_neighbour = f(graph, neighbour)
            f_graph_neighbours.append(f_graph_neighbour) # add to list to use it if no better solution found

            if f_graph_neighbour < f_graph_s:  # if better solution found, stop generating neighbours

                aspiration_for_neighbour = A.setdefault(f_graph_s, f_graph_s-1)
                if moves[-1] not in T or f_graph_neighbour <= aspiration_for_neighbour:
                    # if f_graph_neighbour <= aspiration_for_neighbour and moves[-1] in T: # for test purposes
                    #     print("Tabu ignored (during generating)")
                    #     print(f_graph_s, f_graph_neighbour)
                    A[f_graph_s] = f_graph_neighbour-1

                    s = neighbour
                    T.append(moves[-1])
                    bestFound = True
                    break

        # if no better solution found, choose the best one from neighbours
        if not bestFound:
            minF = float('inf')
            minIdx = None
            for i in range(len(neighbours)):
                # if (f(graph, neighbours[i]) != f_graph_neighbours[i]):
                    # print("Error")
                    # raise Exception
                if moves[i] not in T and f_graph_neighbours[i] < minF:
                    minIdx = i
                    minF = f_graph_neighbours[i]
            if minIdx is None:
                print("All possible moves are in tabu list")
                minIdx = 0
            s = neighbours[minIdx]
            T.append(moves[minIdx]) # add chosen move to tabu list

        moves.clear()

    if f(graph, s) == 0:
        return s
    return None
