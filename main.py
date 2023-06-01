import pygame
import numpy as np
import random
from table import Table
# Initialize Pygame
pygame.init()

# Set up the dimensions of the Sudoku grid
grid_size = 9
cell_size = 60
grid_width = cell_size * grid_size  #540
grid_height = cell_size * grid_size #540
window_width = grid_width + 2
window_height = grid_height + 50

# Set up the colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GRAY = pygame.Color(200, 200, 200)
BLUE = pygame.Color(0, 0, 255)
YELLOW = pygame.Color(250,235,215)
RED = pygame.Color(165,42,42)

# Set up the font
font = pygame.font.Font(None, 36)


# Create the game window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Sudoku Game")

# Create a Sudoku grid
grid = Table(1)


# Create a copy of the initial game grid to track highlighted numbers
highlighted_grid = np.zeros((grid_size, grid_size), dtype=bool)



# Function to draw the Sudoku grid
def draw_grid():
    window.fill(WHITE)

    #draw the lines
    for i in range(grid_size + 1):
        if i % 3 == 0:
            thickness = 2
        else:
            thickness = 1
        pygame.draw.line(window, BLACK, (i * cell_size + 1, 1), (i * cell_size + 1, grid_height + 1), thickness)
        pygame.draw.line(window, BLACK, (1, i * cell_size + 1), (grid_width + 1, i * cell_size + 1), thickness)

    # draw the number
    for i in range(grid_size):
        for j in range(grid_size):

            if grid.table[i][j] != 0:
                text = font.render(str(grid.table[i][j]), True, BLACK)
                text_rect = text.get_rect(center=((j * cell_size) + (cell_size // 2) + 1,
                                                   (i * cell_size) + (cell_size // 2) + 1))
                if grid.highlighted_grid[i][j]:
                    pygame.draw.rect(window, GRAY, (j * cell_size + 1, i * cell_size + 1, cell_size, cell_size))
                window.blit(text, text_rect)
            elif grid.table[i][j] == 0:
                text = font.render(" ", True, BLACK)
                text_rect = text.get_rect(center=((j * cell_size) + (cell_size // 2) + 1,
                                                  (i * cell_size) + (cell_size // 2) + 1))
                if grid.highlighted_grid[i][j]:
                    pygame.draw.rect(window, YELLOW, (j * cell_size + 1, i * cell_size + 1, cell_size, cell_size))
                window.blit(text, text_rect)









# Game loop
running = True
while running:
    grid.handle_events()
    draw_grid()
    pygame.display.update()



