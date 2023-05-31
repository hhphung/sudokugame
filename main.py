import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Set up the dimensions of the Sudoku grid
grid_size = 9
cell_size = 60
grid_width = cell_size * grid_size
grid_height = cell_size * grid_size
window_width = grid_width + 2
window_height = grid_height + 2

# Set up the colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GRAY = pygame.Color(200, 200, 200)
BLUE = pygame.Color(0, 0, 255)
YELLOW = pygame.Color(255, 255, 0)

# Set up the font
font = pygame.font.Font(None, 36)

# Create the game window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Sudoku Game")

# Create an example Sudoku grid
grid = np.array([
    [0, 0, 0, 0, 0, 0, 0, 9, 2],
    [0, 9, 8, 0, 4, 2, 0, 0, 0],
    [0, 0, 0, 0, 6, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 0, 4],
    [0, 0, 0, 2, 0, 7, 0, 0, 0],
    [0, 4, 0, 8, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 1, 2, 0, 5, 3, 0],
    [2, 7, 0, 0, 0, 0, 0, 0, 0]
])

# Create a copy of the initial game grid to track highlighted numbers
highlighted_grid = np.zeros((grid_size, grid_size), dtype=bool)

# Function to draw the Sudoku grid
def draw_grid():
    window.fill(WHITE)

    for i in range(grid_size + 1):
        if i % 3 == 0:
            thickness = 2
        else:
            thickness = 1
        pygame.draw.line(window, BLACK, (i * cell_size + 1, 1), (i * cell_size + 1, grid_height + 1), thickness)
        pygame.draw.line(window, BLACK, (1, i * cell_size + 1), (grid_width + 1, i * cell_size + 1), thickness)

    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] != 0:
                text = font.render(str(grid[i][j]), True, BLACK)
                text_rect = text.get_rect(center=((j * cell_size) + (cell_size // 2) + 1,
                                                   (i * cell_size) + (cell_size // 2) + 1))
                if highlighted_grid[i][j]:
                    pygame.draw.rect(window, YELLOW, (j * cell_size + 1, i * cell_size + 1, cell_size, cell_size))
                window.blit(text, text_rect)

# Function to handle events
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if x <= grid_width and y <= grid_height:
                col = x // cell_size
                row = y // cell_size
                number = grid[row][col]
                if number != 0:
                    highlighted_grid.fill(False)
                    highlighted_grid[np.where(grid == number)] = True

# Game loop
running = True
while running:
    handle_events()
    draw_grid()
    pygame.display.update()