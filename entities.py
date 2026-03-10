# Defines the Cell and Map classes for the Connect Four game. 
# The Cell class represents each cell in the grid.
# The Map class manages the grid and provides methods to interact with it, such as dropping tokens and retrieving cell states.


class Cell:
    def __init__(self, state):
        self.state = state

class Map:
    def __init__(self, width):
        self.width = width
        self.grid = [[Cell(0) for _ in range(width)] for _ in range(width)]

    def get_cell(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.width:
            return self.grid[y][x]
        else:
            raise IndexError("Coordinates out of bounds")

    def drop_token(self, column, turn):
        for row in range(self.width - 1, -1, -1):
            if self.grid[row][column].state == 0:
                self.grid[row][column].state = turn
                return row
        raise ValueError("Column is full")