import pygame
import random

# Grid settings
WIDTH = 600
HEIGHT = 600
ROWS = 20

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)

def create_grid(rows):
    grid = [[0 for _ in range(rows)] for _ in range(rows)]

    # Add random obstacles
    for i in range(rows):
        for j in range(rows):
            if random.random() < 0.2:
                grid[i][j] = 1  # obstacle

    return grid

def draw_grid(win, rows, width, grid):
    gap = width // rows
    for i in range(rows):
        for j in range(rows):
            color = WHITE
            if grid[i][j] == 1:
                color = BLACK

            pygame.draw.rect(win, color, (j*gap, i*gap, gap, gap))

    # grid lines
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i*gap), (width, i*gap))
        pygame.draw.line(win, GREY, (i*gap, 0), (i*gap, width))

def setup_simulation():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Autonomous Navigation Simulation")

    grid = create_grid(ROWS)

    return win, grid