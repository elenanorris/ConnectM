import math
import copy
def a_b_search(board, depth, alpha, beta, maximizing, connect):
    if board.has_connect(1, connect):
        return 1000 + depth, None
    if board.has_connect(2, connect):
        return -1000 - depth, None
    if depth == 0 or board.is_full():
        return evaluate(board, connect), None
    valid = board.available_columns()

    if maximizing:
        value = -math.inf
        best_move = valid[0]

        for c in valid:
            new_board = copy.deepcopy(board)
            new_board.drop_token(c, 1)
            new_score, _ = a_b_search(new_board, depth - 1, alpha, beta, False, connect)
            if new_score > value:
                value = new_score
                best_move = c
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value, best_move
    else:
        value = math.inf
        best_move = valid[0]

        for c in valid:
            new_board = copy.deepcopy(board)
            new_board.drop_token(c, 2)
            new_score, _ = a_b_search(new_board, depth - 1, alpha, beta, True, connect)
            if new_score < value:
                value = new_score
                best_move = c
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value, best_move

def evaluate(board, connect):
    score = 0
    board_size = board.width
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]

    for row in range(board_size):
        for col in range(board_size):
            for col_step, row_step in directions:
                # Skip if the window of length M would go out of bounds.
                window_end_col = col + col_step * (connect - 1)
                window_end_row = row + row_step * (connect - 1)
                if window_end_col < 0 or window_end_col >= board_size or window_end_row < 0 or window_end_row >= board_size:
                    continue

                human_tokens = 0
                computer_tokens = 0
                for offset in range(connect):
                    cell_state = board.grid[row + row_step * offset][col + col_step * offset].state
                    if cell_state == 1:
                        human_tokens += 1
                    elif cell_state == 2:
                        computer_tokens += 1

                # A window containing both players' tokens can never lead to a win.
                if human_tokens > 0 and computer_tokens > 0:
                    continue

                if human_tokens > 0:
                    score += 2 ** human_tokens
                elif computer_tokens > 0:
                    score -= 2 ** computer_tokens

    return score