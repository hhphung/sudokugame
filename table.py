
import random
import pygame
import numpy as np

class Table:
    def __init__(self,level):
        self.numbers = level * 13
        self.grid_size = 9
        self.cell_size = 60
        self.grid_width = self.cell_size * self.grid_size  # 540
        self.grid_height = self.cell_size * self.grid_size  # 540
        self.goal_table = self.generate_sudoku_grid()
        self.table = self.generate_table_game()
        self.wrongs_grid = np.zeros((self.grid_size, self.grid_size), dtype=bool)
        self.highlighted_grid = np.zeros((self.grid_size, self.grid_size), dtype=bool)
        self.hightlightpos = (-1,-1)
    def generate_sudoku_grid(self):
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





# Function to handle events
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if x <= self.grid_width and y <= self.grid_height:
                    col = x // self.cell_size
                    row = y // self.cell_size
                    number = self.table[row][col]

                    if number != 0:
                        self.highlighted_grid.fill(False)
                        self.highlighted_grid[np.where(self.table == number)] = True
                        self.hightlightpos = (-1,1)

                    elif number == 0:
                        self.highlighted_grid.fill(False)
                        self.highlighted_grid[row][col] = True
                        self.hightlightpos = (row, col)
            elif event.type == pygame.KEYDOWN and self.hightlightpos != (-1,1):
                pos = self.hightlightpos
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    self.table[pos[0]] [pos[1]] = 1
                elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    self.table[pos[0]] [pos[1]] = 2
                elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    self.table[pos[0]] [pos[1]] = 3
                elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    self.table[pos[0]] [pos[1]] = 4
                elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    self.table[pos[0]] [pos[1]] = 5
                elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    self.table[pos[0]] [pos[1]] = 6
                elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    self.table[pos[0]] [pos[1]] = 7
                elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    self.table[pos[0]] [pos[1]] = 8
                elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    self.table[pos[0]] [pos[1]] = 9

                self.highlighted_grid[pos[0]][pos[1]] = False
                self.check_number(pos[0], pos[1])
                self.hightlightpos = (-1, -1)


    def check_number(self, row, col):
        if self.table[row][col] == self.goal_table[row][col]:
            self.numbers -=1;
            self.wrongs_grid[row][col] = False
            return
        self.wrongs_grid[row][col] = True





    def generate_table_game(self):
        grid = np.zeros((9, 9), dtype=int)
        #generate the random pair of spot for our game
        def create_number_missing_spot():
            result = []
            i = 0
            while i < self.numbers:
                arr = (random.randint(0,8), random.randint(0,8))
                if arr not in result:
                    result.append(arr)
                    i+=1
            return result

        pairs = create_number_missing_spot()
        for i in range (0,9):
            for j in range(0,9):
                if(i,j) not in pairs:
                    grid[i][j] = self.goal_table[i][j]
        return grid









