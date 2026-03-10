# Command line entrypoint for Connect M.
# This file contains the main game loop and argument parsing.
# Usage:
#     python connectM.py N M H

# Arguments:
#    N: board size (NxN)
#    M: contiguous token count needed to win
#    H: who goes first (1 = human, 0 = computer)


import random
import sys

from UI import UI
from entities import Map


def print_usage():
    print("Usage: python connectM.py N M H")
    print("  N: board size (NxN), integer >= 1")
    print("  M: contiguous count to win, integer in [1, N]")
    print("  H: first player flag (1 = human, 0 = computer)")


def parse_args(argv):
    if len(argv) != 3:
        print_usage()
        return None

    try:
        board_size = int(argv[0])
        connect_count = int(argv[1])
        human_first = int(argv[2])
    except ValueError:
        print("Error: N, M, and H must all be integers.")
        print_usage()
        return None

    if board_size < 1:
        print("Error: N must be at least 1.")
        return None

    if connect_count < 1 or connect_count > board_size:
        print("Error: M must be between 1 and N.")
        return None

    if human_first not in (0, 1):
        print("Error: H must be 0 or 1.")
        return None

    return board_size, connect_count, human_first

# Placeholder for the computer's move selection logic. This will eventually use the alpha-beta search algorithm to choose the best move.
def choose_computer_move(board):
    return random.choice(board.available_columns())


def run_game(board_size, connect_count, human_first):
    ui = UI()
    board = Map(board_size)
    current_player = 1 if human_first == 1 else 2

    print(
        "Starting Connect M on a {}x{} board. Connect {} to win.".format(
            board_size, board_size, connect_count
        )
    )
    print("Player is X, computer is O.")

    while True:
        ui.display_board(board)

        if current_player == 1:
            column = ui.prompt_human_move(board.width)
            if column is None:
                print("Game ended by player.")
                return 0
        else:
            column = choose_computer_move(board)
            print("Computer chooses column {}".format(column + 1))

        try:
            board.drop_token(column, current_player)
        except ValueError:
            # Computer fallback if random pick hits a full column.
            if current_player == 2 and board.available_columns():
                continue
            print("That column is full. Try another column.")
            continue

        if board.has_connect(current_player, connect_count):
            ui.display_board(board)
            if current_player == 1:
                print("You win!")
            else:
                print("Computer wins.")
            return 0

        if board.is_full():
            ui.display_board(board)
            print("Draw. The board is full.")
            return 0

        current_player = 2 if current_player == 1 else 1


def main(argv=None):
    args = argv if argv is not None else sys.argv[1:]
    parsed = parse_args(args)
    if parsed is None:
        return 2

    board_size, connect_count, human_first = parsed
    return run_game(board_size, connect_count, human_first)


if __name__ == "__main__":
    raise SystemExit(main())