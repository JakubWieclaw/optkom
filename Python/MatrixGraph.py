import random

class MatrixGraph():
    """
    ignoring n if filename is given
    """
    def __init__(self, n : int, filename : str =None, vertices_from_zero_in_file : bool =False, directed : bool =False):
        self.directed = directed
        self.edge_count = 0
        self.nodes_set = set()

        if filename:
            with open(filename, "r") as f:
                self.size = int(next(f))
                self.n_and_e = [[0]*self.size for _ in range(self.size)]
                for line in f:
                    line = line.split()
                    if len(line) == 2:
                        if vertices_from_zero_in_file:
                            self.add_edge(int(line[0]), int(line[1]))
                            self.nodes_set.add(int(line[0]))
                            self.nodes_set.add(int(line[1]))
                        else:
                            self.add_edge(int(line[0])-1, int(line[1])-1)
                            self.nodes_set.add(int(line[0])-1)
                            self.nodes_set.add(int(line[1])-1)
        else:
            self.n_and_e = [[0]*n for _ in range(n)]
            self.size = n

    def __str__(self):
        string = ""
        for r in self.n_and_e:
            for c in r:
                string += str(c) + " "
            string += "\n"
        return string

    def nodes(self):
        return self.nodes_set

    def add_edge(self, v : int, w : int, weight : int =1):
        if self.n_and_e[v][w] != 0:
            print (f"Edge already exists {v} {w}")
            # raise RuntimeError("Added already existing edge")  # Just in case
        self.nodes_set.add(v)
        self.nodes_set.add(w)
        if self.directed:
            self.edge_count += 1
            self.n_and_e[v][w] = weight
        else:
            self.n_and_e[v][w] = weight
            self.n_and_e[w][v] = weight
            self.edge_count += 1

    def successors(self, v : int):
        s = []
        for i in range(len(self.n_and_e)):
            if self.n_and_e[v][i] != 0:
                s.append(i)
        return s
        # return [i for i, x in enumerate(self.n_and_e[v]) if x == 1]

    def add_edges_from_list(self, l : list):
        for item in l:
            self.add_edge(*item)

    def number_of_nodes(self):
        return len(self.nodes_set)

    def get_weight(self, v : int, w : int):
        return self.n_and_e[v][w]

    def get_node_with_min_degree(self):
        min_degree = float("inf")
        min_degree_node = None
        for node in self.nodes_set:
            degree = len(self.successors(node))
            if degree < min_degree:
                min_degree = degree
                min_degree_node = node
        return min_degree_node

    def remove_node(self, node : int):
        self.nodes_set.remove(node)
        for i in range(self.size):
            self.n_and_e[node][i] = 0
            self.n_and_e[i][node] = 0
        # self.size -= 1

    def is_edge(self, v : int, w : int):
        return self.n_and_e[v][w] == 1

    def generate_random_graph(self, p : float):
        for i in range(self.size):
            for j in range(self.size):
                if i != j:
                    if random.random() < p:
                        self.add_edge(i, j)

    def save_to_file(self, filename : str):
        with open(filename, "w") as f:
            f.write(str(self.size))
            f.write("\n")
            for i in range(self.size):
                for j in range(i+1, self.size):
                    if self.n_and_e[i][j] == 1:
                        f.write(f"{i} {j}\n")