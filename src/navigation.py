import pygame
import time

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

def draw_path(win, path, rows, width):
    gap = width // rows
    for node in path:
        pygame.draw.rect(win, GREEN, (node[1]*gap, node[0]*gap, gap, gap))

def draw_agent(win, pos, rows, width):
    gap = width // rows
    pygame.draw.rect(win, BLUE, (pos[1]*gap, pos[0]*gap, gap, gap))

def move_agent(win, path, draw_func, rows, width, grid):
    for pos in path:
        win.fill((255,255,255))
        draw_func(win, rows, width, grid)
        draw_path(win, path, rows, width)
        draw_agent(win, pos, rows, width)
        pygame.display.update()
        time.sleep(0.1)