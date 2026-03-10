def print_board(board):
    width = board.width
    for row in range(width):
        print("+---" * width + "+")
        for col in range(width):
            state = board.grid[row][col].state
            if state == 1:
                symbol = "X"
            elif state == -1:
                symbol = "O"
            else:
                symbol = " "
            print(f"| {symbol} ", endl="")
        print("|")
    print("+---" * width + "+")
    for i in range(width):
        print(f"  {i} ", end="")
    print("\n")