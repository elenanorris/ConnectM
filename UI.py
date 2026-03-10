# CMD based UI for the Connect M game. This will hold functions for validating inputs and allow user 
# the option to quit the game at any time.

class UI:
    def __init__(self):
        pass

    def display_board(self, map):
        symbols = {0: '.', 1: 'X', 2: 'O'}
        header = ' '.join([str(i + 1) for i in range(map.width)])
        print(header)
        for row in map.grid:
            print(' '.join([symbols[cell.state] for cell in row]))

    def check_if_player_quit(self, input):
        if input.lower() == 'quit' or input.lower() == 'q':
            return True
        return False

    def prompt_human_move(self, width):
        while True:
            user_input = input("Choose a column (1-{}), or 'q' to quit: ".format(width)).strip()

            if self.check_if_player_quit(user_input):
                return None

            if not user_input.isdigit():
                print("Invalid input. Enter a number or 'q' to quit.")
                continue

            column = int(user_input)
            if column < 1 or column > width:
                print("Column out of range. Choose between 1 and {}.".format(width))
                continue

            return column - 1