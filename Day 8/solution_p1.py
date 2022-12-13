def traverse(i, j, grid):
    max_left = 0
    max_right = 0
    max_up = 0
    max_down = 0
    for left in range(0, j):
        max_left = max(grid[i][left], max_left)
    for right in range(j + 1, len(grid[i])):
        max_right = max(grid[i][right], max_right)
    for up in range(0, i):
        max_up = max(grid[up][j], max_up)
    for down in range(i + 1, len(grid)):
        max_down = max(grid[down][j], max_down)
    if max_down < grid[i][j] or max_left < grid[i][j] or max_right < grid[i][j] or max_up < grid[i][j]:
        return 1
    return 0


with open('input.txt') as f:
    grid = []
    for line in f:
        line = line[:-1]
        grid.append(list(map(int, list(line))))
    visible = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[i]) - 1:
                visible += 1
            else:
                visible += traverse(i, j, grid)
    print(visible)
