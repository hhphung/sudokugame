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
            string = str(grid.table[i][j])
            text = font.render(string if grid.table[i][j]> 0 else " ", True, BLACK)
            text_rect = text.get_rect(center=((j * cell_size) + (cell_size // 2) + 1,
                                              (i * cell_size) + (cell_size // 2) + 1))


            if grid.table[i][j] != 0:
                if grid.highlighted_grid[i][j]:
                    pygame.draw.rect(window, GRAY, (j * cell_size + 1, i * cell_size + 1, cell_size, cell_size))
                window.blit(text, text_rect)
            if grid.wrongs_grid[i][j]:
                pygame.draw.rect(window, RED, (j * cell_size + 1, i * cell_size + 1, cell_size, cell_size))
                window.blit(text, text_rect)
            elif grid.table[i][j] == 0:
                if grid.highlighted_grid[i][j]:
                    pygame.draw.rect(window, YELLOW, (j * cell_size + 1, i * cell_size + 1, cell_size, cell_size))
                window.blit(text, text_rect)
        # Draw the count
        count_text = font.render("Chance: " + str(grid.lives), True, BLACK)
        count_rect = count_text.get_rect(bottomleft=(10, window.get_height() - 10))
        window.blit(count_text, count_rect)

#draw the game windown if the player won the game
def draw_win_window():
    win_window_width = 200
    win_window_height = 100
    win_window = pygame.Surface((win_window_width, win_window_height))
    win_window_rect = win_window.get_rect(center=(window_width // 2, window_height // 2))
    win_window.fill(WHITE)
    win_text = font.render("You Win!", True, BLACK)
    win_text_rect = win_text.get_rect(center=(win_window_width // 2, win_window_height // 2))
    win_window.blit(win_text, win_text_rect)
    window.blit(win_window, win_window_rect)

# draw the game windown if the player lost the game
def draw_lost_windown():
    lose_window_width = 200
    lose_window_height = 100
    lose_window = pygame.Surface((lose_window_width, lose_window_height))
    lose_window_rect = lose_window.get_rect(center=(window_width // 2, window_height // 2))
    lose_window.fill(WHITE)
    lose_text = font.render("You Lost!", True, BLACK)
    lose_text_rect = lose_text.get_rect(center=(lose_window_width // 2, lose_window_height // 2))
    lose_window.blit(lose_text, lose_text_rect)
    window.blit(lose_window, lose_window_rect)


# Game loop

game_over = False
while True:
    grid.handle_events()
    if not grid.win() and not grid.lose():
        draw_grid()
    else:
        draw_grid()
        if grid.win():
            draw_win_window()
        elif grid.lose():
            draw_lost_windown()
    pygame.display.update()



