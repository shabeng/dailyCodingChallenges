import numpy as np
from DijkstraAlgorithm.graph import Graph


def dijkstra(graph: Graph, start_node, end_node):
    # Check that the nodes are in the graph
    start_ex = graph.is_node(start_node)
    end_ex = graph.is_node(end_node)
    if not start_ex or not end_ex:
        return f'There is no node that correspond to the start or the end nodes: S: {start_ex} , E: {end_ex}'

    # Init
    not_visited_nodes = []
    shortest_dist = {}
    prev_node = {}
    n = len(graph.get_nodes_list())

    for v in graph.get_nodes_list():
        shortest_dist[v] = np.infty
        prev_node[v] = None
        not_visited_nodes.append(v)

    shortest_dist[start_node] = 0
    prev_node[start_node] = start_node

    # Explore graph nodes
    while len(not_visited_nodes) != 0:
        v = min(not_visited_nodes, key=shortest_dist.get)
        not_visited_nodes.remove(v)
        for neighbor in graph.get_node_neighbors(v):
            alt_dist = shortest_dist[v] + graph.get_edge_weight(v, neighbor)
            if alt_dist < shortest_dist[neighbor]:
                shortest_dist[neighbor] = alt_dist
                prev_node[neighbor] = v

    return shortest_dist, prev_node


def create_path(prev_node_dict, start_node, end_node):
    curr_node = end_node
    path = [curr_node]
    while curr_node != start_node:
        curr_node = prev_node_dict[curr_node]
        path.append(curr_node)
    return path[::-1]


if __name__ == '__main__':
    edges = [((1, 2), 4), ((1, 3), 3), ((2, 3), 2), ((2, 4), 5), ((3, 5), 10),
             ((4, 5), 1), ((4, 6), 4), ((5, 6), 1)]
    graph_test = Graph(edges, is_directed=False)
    spd, prv_nd = dijkstra(graph_test, 1, 6)
    print(spd)
    print(prv_nd)
    print(create_path(prv_nd, 1, 6))



