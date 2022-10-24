import networkx as nx
import matplotlib.pyplot as plt

# Just a wrapper for networkx.Graph
# Maybe to be extended later
class Graph(nx.Graph):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def create_graph_from_dr_machowiaks_file(self, filename: str, nodes_counting_from_zero=False) -> None:
        """Overwrite existing graph with a new graph from Dr Machowiak's file"""
        if (self.number_of_nodes() > 0):
            self.clear()
            print("Overwriting existing graph with a new graph from Dr Machowiak's file")
        with open(filename, 'r') as file:
            next(file) # skip first line
            for line in file:
                line = line.split()
                line = [int(node) for node in line]
                if not nodes_counting_from_zero: # in this program nodes NEED TO be counted from zero
                    line[0] -= 1
                    line[1] -= 1
                if len(line) == 2:
                    self.add_edges_from([tuple(line)])

    def generate_random_simple_graph(self, nodes : int, probability_of_edge_creation : float) -> None:
        """Overwrite existing graph with a new random graph (create if not exist)"""
        if (self.number_of_nodes() > 0):
            self.clear()
            print("Overwriting existing graph with a new random graph")
        self.update(nx.fast_gnp_random_graph(nodes, probability_of_edge_creation))

    def draw(self, colors={}, *args, **kwargs) -> None:
        """Drawing the graph with matplotlib"""
        # TODO: repair node coloring
        # if colors:
        #     colors_list = [item[1] for item in sorted(colors.items(), key=lambda item: item[0])]
        #     print(colors_list)
        #     nx.draw_networkx(self, node_color=colors_list, *args, **kwargs)
        # else:
        nx.draw_networkx(self, *args, **kwargs)
        plt.show()

    def save_to_txt_file(self, filename : str):
        with open(filename, "w+") as f:
            f.write(f"{self.number_of_nodes()}\n")
            used_edges = list()
            for item in self.edges():
                if item in used_edges or (item[1], item[0]) in used_edges:
                    continue
                f.write(f"{item[0]} {item[1]}\n") # count nodes from zero
                used_edges.append(item)
