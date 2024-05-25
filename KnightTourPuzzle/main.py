from KnightTourPuzzle.chess_board_class import ChessBoardPlay
from KnightTourPuzzle.backtracking import backtracking_knight_route, copy_cb_obj

import numpy as np
import time

# Perform one puzzle:
possible_steps_all = [(-1, -2), (1, -2), (2, -1), (2, 1), (-1, 2), (1, 2), (-2, -1), (-2, 1)]
board_dim = 5
board = ChessBoardPlay(board_dim, possible_steps_all)
print(f'First position: {board.get_curr_loc()}')
partial_sol = []
s1_time = time.time()
route, all_routes = backtracking_knight_route(board, partial_sol)
e1_time = time.time()
print(f'Total time to calc Exp #1: {e1_time - s1_time} seconds. ')
board.print_route_on_board(route)

# Create the number of solutions for each starting point:
board_sols_num = np.zeros((board_dim, board_dim))
s2_time = time.time()
for i in range(board_dim):
    for j in range(board_dim):
        print(f'Starting ({i}, {j})')
        sij_time = time.time()
        board = ChessBoardPlay(board_dim, possible_steps_all, sample_first_pos=False, first_pos=(i, j))
        partial_sol = []
        _, all_routes = backtracking_knight_route(board, partial_sol)
        board_sols_num[i, j] = len(all_routes)
        eij_time = time.time()
        print(f'Finished ({i}, {j}): {eij_time - sij_time} seconds. ')
e2_time = time.time()
print(f'Total time to calc Exp #2: {(e2_time - s2_time) / 60} minutes. ')
print(board_sols_num)



