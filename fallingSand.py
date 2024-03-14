import pygame
import random

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
w = 5
cols = WINDOW_WIDTH // w
rows = WINDOW_HEIGHT // w
hue_value = 2

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Create grid function
def make_2d_array(rows, cols):
    return [[0] * cols for _ in range(rows)]

grid = make_2d_array(rows, cols)
grid[5][32] = 1
hue_selector = 0
# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                hue_selector += 1
            if hue_selector > 2:
                hue_selector = 0
    # Mouse interaction
    mouse_col, mouse_row = pygame.mouse.get_pos()
    mouse_col = mouse_col // w
    mouse_row = mouse_row // w
    matrix = 5
    extent = matrix // 2
    for i in range(-extent, extent + 1):
        for j in range(-extent, extent + 1):
            if random.random() < 0.1:
                col = mouse_col + i
                row = mouse_row + j
                if 0 <= col < cols and 0 <= row < rows:
                    grid[row][col] = hue_value #initiatiazion with different hues

    if hue_value < 200:
        hue_value += 1
    else:
        hue_value = 2

    # Update display
    screen.fill(BLACK)


    # Update grid
    next_grid = make_2d_array(rows, cols)
    for i in range(cols):
        for j in range(rows):
            state = grid[j][i]
            if state > 0:
                below = grid[j + 1][i] if j < rows - 1 else None

                direction = 1 if random.random() < 0.5 else -1
                below_a = grid[j + 1][i + direction] if j < rows - 1 and 0 <= i + direction < cols else None
                below_b = grid[j + 1][i - direction] if j < rows - 1 and 0 <= i - direction < cols else None

                if below == 0:
                    next_grid[j][i] = 0
                    next_grid[j + 1][i] = grid[j][i]
                elif below_a == 0:
                    next_grid[j + 1][i + direction] = grid[j][i]
                elif below_b == 0:
                    next_grid[j + 1][i - direction] = grid[j][i]
                else:
                    next_grid[j][i] = grid[j][i]
    for i in range(cols):
        for j in range(rows):
            if hue_selector == 0:
                color = (grid[j][i], 255,255)
            if hue_selector == 1:
                color = (grid[j][i],255,255)

            if hue_selector == 2:
                color = (255, 255, grid[j][i])

            if grid[j][i] > 1:
                pygame.draw.rect(screen, color, (i * w, j * w, w, w))

    grid = next_grid

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
