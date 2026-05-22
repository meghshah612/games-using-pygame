from .pieces import convert_shape_format
from .config import GRID_COLUMNS, GRID_ROWS


def create_grid(locked_positions=None):
    if locked_positions is None:
        locked_positions = {}

    grid = [[(0, 0, 0) for _ in range(GRID_COLUMNS)] for _ in range(GRID_ROWS)]

    for i in range(GRID_ROWS):
        for j in range(GRID_COLUMNS):
            if (j, i) in locked_positions:
                grid[i][j] = locked_positions[(j, i)]

    return grid


def valid_space(piece, grid):
    accepted_positions = [
        (j, i)
        for i in range(GRID_ROWS)
        for j in range(GRID_COLUMNS)
        if grid[i][j] == (0, 0, 0)
    ]

    formatted = convert_shape_format(piece)

    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False
    return True


def check_lost(positions):
    return any(y < 1 for _, y in positions)


def clear_rows(grid, locked):
    rows_cleared = 0
    for i in range(len(grid) - 1, -1, -1):
        if (0, 0, 0) not in grid[i]:
            rows_cleared += 1
            for j in range(len(grid[i])):
                locked.pop((j, i), None)

    if rows_cleared > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < i:
                locked[(x, y + rows_cleared)] = locked.pop(key)

    return rows_cleared
