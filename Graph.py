import networkx as nx
import matplotlib.pyplot as plt

# Just a wrapper for networkx.Graph
# Maybe to be extended later
class Graph(nx.Graph):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # nx.set_node_attributes(self, 0, 'color')

    def generate_random_simple_graph(self, nodes : int, probability_of_edge_creation : float) -> None:
        """Overwrite existing graph with a new random graph (create if not exist)"""
        if (self.number_of_nodes() > 0):
            self.clear()
            print("Overwriting existing graph with a new random graph")
        self.update(nx.fast_gnp_random_graph(nodes, probability_of_edge_creation))

    def draw(self):
        """Drawing the graph with matplotlib"""
        nx.draw_networkx(self)
        plt.show()
