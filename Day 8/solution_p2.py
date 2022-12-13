def traverse(i, j, grid):
    max_left = 0
    max_right = 0
    max_up = 0
    max_down = 0
    for left in range(j - 1, -1, -1):
        max_left += 1
        if grid[i][left] >= grid[i][j]:
            break
    for right in range(j + 1, len(grid[i])):
        max_right += 1
        if grid[i][right] >= grid[i][j]:
            break
    for up in range(i - 1, -1, -1):
        max_up += 1
        if grid[up][j] >= grid[i][j]:
            break
    for down in range(i + 1, len(grid)):
        max_down += 1
        if grid[down][j] >= grid[i][j]:
            break
    return max_down * max_left * max_right * max_up


with open('input.txt') as f:
    grid = []
    for line in f:
        line = line[:-1]
        grid.append(list(map(int, list(line))))
    scenic_score = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            scenic_score = max(scenic_score, traverse(i, j, grid))
    print(scenic_score)
