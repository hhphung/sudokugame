import numpy as np
import random


def generate_sudoku_grid():
    grid = np.zeros((9, 9), dtype=int)

    # Function to check if a number is valid at a given position
    def is_valid_number(grid, row, col, number):
        # Check row
        if number in grid[row]:
            return False

        # Check column
        if number in grid[:, col]:
            return False

        # Check 3x3 subgrid
        subgrid_row = (row // 3) * 3
        subgrid_col = (col // 3) * 3
        subgrid = grid[subgrid_row:subgrid_row+3, subgrid_col:subgrid_col+3]
        if number in subgrid:
            return False

        return True

    # Function to solve the Sudoku grid using backtracking
    def solve_sudoku(grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for number in random.sample(range(1, 10), 9):
                        if is_valid_number(grid, row, col, number):
                            grid[row][col] = number
                            if solve_sudoku(grid):
                                return True
                            grid[row][col] = 0
                    return False
        return True

    # Generate a complete Sudoku grid
    solve_sudoku(grid)

    # Fill all empty cells with valid numbers
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for number in range(1, 10):
                    if is_valid_number(grid, row, col, number):
                        grid[row][col] = number
                        break

    return grid

# Generate a valid Sudoku grid with filled empty cells
sudoku_grid = generate_sudoku_grid()

# Print the generated grid
print(sudoku_grid)
