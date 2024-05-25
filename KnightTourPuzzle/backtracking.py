from KnightTourPuzzle.chess_board_class import ChessBoardPlay


def backtracking_knight_route(cb: ChessBoardPlay, partial_sol: list):
    cache_sols = []

    def backtracking_helper(cb: ChessBoardPlay, partial_sol: list):
        candidate_steps = cb.calc_possible_steps()

        if cb.is_all_visited():
            cache_sols.append(partial_sol)
            return partial_sol

        for candidate_step in candidate_steps:
            next_x, next_y = cb.curr_loc_x + candidate_step[0], cb.curr_loc_y + candidate_step[1]
            partial_sol_new = partial_sol[:]
            partial_sol_new.append((next_x, next_y))
            new_cb = copy_cb_obj(cb)
            new_cb.sign_visited_place((next_x, next_y))
            backtracking_helper(new_cb, partial_sol_new)

        return

    partial_sol = [cb.get_curr_loc()]
    backtracking_helper(cb, partial_sol)
    route = cache_sols[0] if len(cache_sols) > 0 else None
    return route, cache_sols


def copy_cb_obj(cb_obj):
    new_cb = ChessBoardPlay(cb_obj.cb_dim, cb_obj.cb_steps)
    new_cb.cb_board = cb_obj.cb_board.copy()
    new_cb.curr_loc_x, new_cb.curr_loc_y = cb_obj.curr_loc_x, cb_obj.curr_loc_y
    return new_cb


if __name__ == '__main__':
    pssbl_stps_all = [(-1, -2), (1, -2), (2, -1), (2, 1), (-1, 2), (1, 2), (-2, -1), (-2, 1)]
    chsbrd = ChessBoardPlay(5, pssbl_stps_all)
    print(chsbrd)
    print(chsbrd.get_curr_loc())
    route, all_routes = backtracking_knight_route(chsbrd, [])
    chsbrd.print_route_on_board(route)
