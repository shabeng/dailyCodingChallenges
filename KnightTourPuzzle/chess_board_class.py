import numpy as np


class ChessBoardPlay:
    def __init__(self, n, possible_steps_lst):
        self.cb_dim = n
        self.cb_board = np.zeros((n, n))
        self.curr_loc_x, self.curr_loc_y = self.sample_start_point()
        self.cb_steps = possible_steps_lst
        self.cb_board_route = np.zeros((n, n))

    def __repr__(self):
        return str(self.cb_board)

    def sample_start_point(self):
        i_start, j_start = np.random.randint(self.cb_dim, size=2)
        self.sign_visited_place((i_start, j_start))
        return i_start, j_start

    def is_in_board(self, x_loc, y_loc):
        loc_not_too_high = x_loc < self.cb_dim and y_loc < self.cb_dim
        loc_not_too_low = x_loc >= 0 and y_loc >= 0
        return loc_not_too_low and loc_not_too_high

    def is_all_visited(self):
        return np.all(self.cb_board == 1)

    def is_one_visited(self, place):
        if self.cb_board[place[0], place[1]] == 1:
            return True
        else:
            return False

    def get_curr_loc(self):
        return self.curr_loc_x, self.curr_loc_y

    def sign_visited_place(self, place_ind):
        if not self.is_in_board(*place_ind):
            raise TypeError(f'Wrong place index: {place_ind} must be '
                            f'within (smaller than) {self.cb_board.shape} and (larger than) 0')
        else:
            self.cb_board[place_ind] = 1
            self.curr_loc_x, self.curr_loc_y = place_ind

    def calc_possible_steps(self):
        pssbl_stps = []
        for step in self.cb_steps:
            new_loc_x, new_loc_y = self.curr_loc_x + step[0], self.curr_loc_y + step[1]
            if self.is_in_board(new_loc_x, new_loc_y):
                if not self.is_one_visited((new_loc_x, new_loc_y)):
                    pssbl_stps.append(step)
        return pssbl_stps

    def print_route_on_board(self, route_lst):
        if route_lst:
            for step_num, step in enumerate(route_lst):
                self.cb_board_route[step] = step_num + 1
            print(self.cb_board_route)
        else:
            print(route_lst)
        return



if __name__ == '__main__':
    pssbl_stps_all = [(-1, -2), (1, -2), (2, -1), (2, 1), (-1, 2), (1, 2), (-2, -1), (-2, 1)]
    cb = ChessBoardPlay(5, pssbl_stps_all)
    # cb.sign_visited_place((4, 4))
    # cb.sign_visited_place((1, 3))
    # i, j = cb.sample_start_point()
    pssbl_stps = cb.calc_possible_steps()
    print(cb)
    print(cb.curr_loc_x, cb.curr_loc_y)
    # print(i, j)
    print(pssbl_stps)
