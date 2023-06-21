def gridChallenge(grid):
    #...
    for i in range(len(grid)):
        grid[i] = list(grid[i])
        grid[i].sort()

    grid_list = list(zip(*grid))

    for i in grid_list:
        if list(i) != sorted(i):
            return "NO"

    return "YES"



t = int(input().strip())

for i in range(t):
    n = int(input().strip())

    grid = []

    for j in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = gridChallenge(grid)

    print(result)
