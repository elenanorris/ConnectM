# Defines the Cell and Map classes for the Connect M game. 
# The Cell class represents each cell in the grid.
# The Map class manages the grid and provides methods to interact with it, such as dropping tokens and retrieving cell states.
# The Map class will also handle win conditions.


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

# Drops a token for the given turn (player) in the specified column.
    def drop_token(self, column, turn):
        for row in range(self.width - 1, -1, -1):
            if self.grid[row][column].state == 0:
                self.grid[row][column].state = turn
                return row
        raise ValueError("Column is full")

    def available_columns(self):
        cols = []
        for column in range(self.width):
            if self.grid[0][column].state == 0:
                cols.append(column)
        return cols

    def is_full(self):
        return len(self.available_columns()) == 0

    def has_connect(self, player, connect_count):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]

        for y in range(self.width):
            for x in range(self.width):
                if self.grid[y][x].state != player:
                    continue

                for dx, dy in directions:
                    if self.has_line_from(x, y, dx, dy, player, connect_count):
                        return True

        return False

    def has_line_from(self, x, y, dx, dy, player, connect_count):
        for step in range(connect_count):
            nx = x + (dx * step)
            ny = y + (dy * step)

            if nx < 0 or ny < 0 or nx >= self.width or ny >= self.width:
                return False

            if self.grid[ny][nx].state != player:
                return False

        return True

    def __repr__(self):
        return '\n'.join([' '.join([str(cell.state) for cell in row]) for row in self.grid])