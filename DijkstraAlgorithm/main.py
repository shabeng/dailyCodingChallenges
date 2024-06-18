import numpy as np
import time
from collections import defaultdict

from DijkstraAlgorithm.graph import create_random_graph
from DijkstraAlgorithm.dijkstra_algorithm import dijkstra_dict, dijkstra_heap, create_path

runs_num = 1000
nodes_num = 1000
edges_num = 100000
runtimes = defaultdict(list)

for i in range(runs_num):
    graph = create_random_graph(nodes_num, edges_num, is_directed=False)
    s_node, e_node = np.random.choice(graph.get_nodes_list(), size=2)
    sols_to_check = []
    for func in [dijkstra_dict, dijkstra_heap]:
        start_t = time.time()
        spd, prv_nd = dijkstra_dict(graph, s_node, e_node)
        end_t = time.time()

        sol = create_path(prv_nd, s_node, e_node)
        sols_to_check.append(sol)

        func_name = str(func).split()[1]
        runtimes[func_name].append(end_t - start_t)
    # assert sols_to_check[0] == sols_to_check[1], f'Different shortest path! {sols_to_check[0]},\n {sols_to_check[1]}'

for key in runtimes:
    res_array = np.array(runtimes[key])
    mean_res = res_array.mean()
    std_res = res_array.std()
    print(f'{key}: mean time = {mean_res} | sd = {std_res}')
