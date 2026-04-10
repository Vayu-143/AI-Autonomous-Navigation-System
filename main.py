import pygame
from src.simulation import setup_simulation, draw_grid, ROWS, WIDTH
from src.path_planning import astar
from src.navigation import move_agent, draw_path

def main():
    win, grid = setup_simulation()

    start = (0, 0)
    end = (ROWS-1, ROWS-1)

    grid[start[0]][start[1]] = 0
    grid[end[0]][end[1]] = 0

    path = astar(grid, start, end)

    if not path:
        print("❌ No path found! Restart program.")
        return

    # 🔥 MOVE AGENT ONLY ONCE
    move_agent(win, path, draw_grid, ROWS, WIDTH, grid)

    running = True
    while running:
        win.fill((255, 255, 255))
        draw_grid(win, ROWS, WIDTH, grid)
        draw_path(win, path, ROWS, WIDTH)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()