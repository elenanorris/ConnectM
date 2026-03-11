import math
import copy
def a_b_search(board, depth, alpha, beta, maximizing, connect):
    if depth == 0 or board.is_full():
        return evaluate(board), None
    if board.has_connect(1, connect):
        return 1000, None
    if board.has_connect(2, connect):
        return -1000, None
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

def evaluate(board):
    # Placeholder for the evaluation function that assesses the current game state.
    # This function will return a score based on how favorable the position is for the current player.
    score = 0
    for row in board.grid:
        for cell in row:
            if cell.state == 1:
                score += 1
            elif cell.state == 2:
                score -= 1
    return score