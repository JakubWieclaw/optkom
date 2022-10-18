import networkx as nx
import matplotlib.pyplot as plt

# Just a wrapper for networkx.Graph
# Maybe to be extended later
class Graph(nx.Graph):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # nx.set_node_attributes(self, 0, 'color')

    def create_graph_from_dr_machowiaks_file(self, filename: str) -> None:
        """Overwrite existing graph with a new graph from Dr Machowiak's file"""
        if (self.number_of_nodes() > 0):
            self.clear()
            print("Overwriting existing graph with a new graph from Dr Machowiak's file")
        with open(filename, 'r') as file:
            next(file) # skip first line
            for line in file:
                line = line.split()
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
        if colors:
            colors_list = [item[1] for item in sorted(colors.items(), key=lambda item: item[0])]
            nx.draw_networkx(self, node_color=colors_list, *args, **kwargs)
        else:
            nx.draw_networkx(self, *args, **kwargs)
        plt.show()
