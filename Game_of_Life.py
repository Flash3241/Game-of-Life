import time
import os
import random

# Grid size
ROWS = 20
COLS = 40

# Initialize grid with random 0s and 1s
def create_grid(rows, cols):
    return [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

# Count live neighbors
def count_neighbors(grid, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  ( 0, -1),         ( 0, 1),
                  ( 1, -1), ( 1, 0), ( 1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < ROWS and 0 <= ny < COLS:
            count += grid[nx][ny]
    return count

# Update grid based on Game of Life rules
def update_grid(grid):
    new_grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    for i in range(ROWS):
        for j in range(COLS):
            neighbors = count_neighbors(grid, i, j)
            if grid[i][j] == 1:
                new_grid[i][j] = 1 if neighbors in [2, 3] else 0
            else:
                new_grid[i][j] = 1 if neighbors == 3 else 0
    return new_grid

# Print grid
def print_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(''.join(['█' if cell else ' ' for cell in row]))

# Run the Game of Life
def game_of_life():
    grid = create_grid(ROWS, COLS)
    try:
        while True:
            print_grid(grid)
            grid = update_grid(grid)
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("Simulation ended.")

if __name__ == "__main__":
    game_of_life()
