from collections import defaultdict
import numpy as np


class Graph:
    def __init__(self, edges_list, is_directed=False):
        self.graph = defaultdict(dict)
        self.nodes = []
        self.create_nodes_edges(edges_list, is_directed)

    def __repr__(self):
        return f'Node Set = {self.graph.keys()}'

    def create_nodes_edges(self, edges_list, is_directed):
        for edge in edges_list:
            (node1, node2), weight = edge
            self.graph[node1][node2] = weight
            if not is_directed:
                self.graph[node2][node1] = weight
        self.nodes += list(self.graph.keys())
        return

    def is_node(self, node):
        if not self.graph.get(node, None):
            return False
        else:
            return True

    def get_nodes_list(self):
        return self.nodes

    def get_node_neighbors(self, node_name):
        return self.graph[node_name].keys()

    def get_edge_weight(self, from_node, to_node):
        w = self.graph[from_node][to_node]
        return w


def create_random_graph(node_num, edge_num, is_directed=False):
    # Sample edges and save unique only
    edges_sample_with_rep = np.random.randint(node_num, size=(edge_num, 2))
    edges_sample_no_rep = np.unique(edges_sample_with_rep, axis=0)
    # Sample weights
    weight_sample = np.random.randint(25, size=(edges_sample_no_rep.shape[0]))
    # Zip between the weights and edges
    edges = list(zip(edges_sample_no_rep, weight_sample))
    g = Graph(edges, is_directed=is_directed)
    return g


if __name__ == '__main__':
    nodes_num = 5
    edges_num = 10
    graph = create_random_graph(nodes_num, edges_num)


