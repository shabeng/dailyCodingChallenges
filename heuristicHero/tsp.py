import numpy as np
from sklearn.metrics.pairwise import euclidean_distances


class TSP:
    def __init__(self, city_number=10, seed=146):
        self.tsp_rs = np.random.RandomState(seed=seed)
        self.tsp_city_num = city_number
        self.tsp_city_loc = self.tsp_rs.random(size=(self.tsp_city_num, 2))
        self.tsp_tij = euclidean_distances(self.tsp_city_loc)
        self.tsp_solutions_cache = {}
        self.tsp_best_route = []
        self.tsp_best_route_len = np.infty

    def get_tij(self):
        return self.tsp_tij

    def construct_greedy_route_given_start_city(self, first_city):
        curr_route = [first_city]
        prev_city_ind = first_city
        curr_route_len = 0
        while len(curr_route) < self.tsp_city_num:
            # Find un visited cities
            not_visited = list(set(range(self.tsp_city_num)) - set(curr_route))
            # Consider only un visited cities
            t_ij_curr = self.tsp_tij[:, not_visited]
            # The closest un visited city
            min_ind = np.argmin(t_ij_curr[prev_city_ind, :])
            corrected_city_ind = not_visited[min_ind]
            # Update parameters
            curr_route.append(corrected_city_ind)
            curr_route_len += self.tsp_tij[prev_city_ind, corrected_city_ind]
            prev_city_ind = corrected_city_ind

        curr_route_len += self.tsp_tij[prev_city_ind, first_city]
        self.tsp_solutions_cache[len(self.tsp_solutions_cache)] = (curr_route, curr_route_len)
        if curr_route_len < self.tsp_best_route_len:
            self.tsp_best_route = curr_route
            self.tsp_best_route_len = curr_route_len
            assert self.tsp_best_route_len == self.calc_distance_of_route(curr_route), \
                f'Different distance! {self.tsp_best_route_len} , {self.calc_distance_of_route(curr_route)}, {curr_route}'

        return curr_route, curr_route_len

    def construct_greedy_route(self):
        for first_city in range(self.tsp_city_num):
            _, _ = self.construct_greedy_route_given_start_city(first_city)

        return self.tsp_best_route, self.tsp_best_route_len

    def calc_distance_of_route(self, route):
        dist = 0
        for city_ind in range(len(route) - 1):
            from_city = route[city_ind]
            to_city = route[city_ind + 1]
            dist += self.tsp_tij[from_city, to_city]
        dist += self.tsp_tij[route[-1], route[0]]
        return dist

    # def k_opt(self):
    #     curr_val =


if __name__ == '__main__':
    prob = TSP(4)
    print(prob.get_tij())
    prob.construct_greedy_route()
    print(prob.tsp_solutions_cache)

