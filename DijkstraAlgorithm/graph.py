from collections import defaultdict


class Graph:
    def __init__(self, edges_list, is_directed=False):
        self.graph = defaultdict(dict)
        self.create_nodes_edges(edges_list, is_directed)

    def __repr__(self):
        return f'Node Set = {self.graph.keys()}'

    def create_nodes_edges(self, edges_list, is_directed):
        for edge in edges_list:
            (node1, node2), weight = edge
            self.graph[node1][node2] = weight
            if not is_directed:
                self.graph[node2][node1] = weight
        return

    def get_node_neighbors(self, node_name):
        return self.graph[node_name]

    def get_edge_weight(self, from_node, to_node):
        w = self.graph[from_node][to_node]
        return w


if __name__ == '__main__':
    import numpy as np
    nodes_num = 5
    edges_num = 10
    edges_sample = [(np.random.randint(nodes_num, size=2), np.random.randint(25)) for i in range(edges_num)]
    edges = [(edge, w) for edge, w in edges_sample if edge[0] != edge[1]]
    graph = Graph(edges, is_directed=False)
    for elem in edges:
        print(elem)
    for elem in graph.graph.keys():
        print(f'{elem}: {graph.graph[elem]}')


