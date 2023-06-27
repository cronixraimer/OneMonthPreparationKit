def get_neighboring_cells(row, col, rows, cols):
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))
    if row < rows - 1:
        neighbors.append((row + 1, col))
    if col > 0:
        neighbors.append((row, col - 1))
    if col < cols - 1:
        neighbors.append((row, col + 1))
    return neighbors

def boomberMan(r, c, n, grid):
    #comments here
    if n == 1:
        return grid

    if n % 2 == 0:
        return ['O' * c for _ in range(r)]

    grid = [list(row) for row in grid]

    # Simulate the grid state after 1 second
    next_grid = [['O' if cell == '.' else '.' for cell in row] for row in grid]
    grid = next_grid

    # Simulate the grid state after 2 seconds
    next_grid = [['O'] * c for _ in range(r)]
    grid = next_grid

    if n % 4 == 3:
        # Simulate the grid state after 3 seconds
        next_grid = [['.' if cell == 'O' else 'O' for cell in row] for row in grid]


first_multiple_input = input().rstrip().split()

r = int(first_multiple_input[0])

c = int(first_multiple_input[1])

n = int(first_multiple_input[2])

grid = []

for i in range(r):
    grid_item = input()
    grid.append(grid_item)

result = boomberMan(n, r, c, grid)

print(result)
