with open('input.txt') as f:
    grid = []
    initial_state = (0, 0)
    goal_state = (0, 0)
    visited = set()
    lines = f.read().split('\n')
    for i in range(len(lines)):
        row = []
        for j in range(len(lines[0])):
            if lines[i][j] == 'E':
                goal_state = (i, j)
                row.append('z')
            elif lines[i][j] == 'S':
                initial_state = (i, j)
                row.append('a')
            else:
                row.append(lines[i][j])
        grid.append(row)
    queue = [(initial_state, 0)]
    shortest_distance = 0
    while len(queue) > 0:
        current_state, distance = queue.pop(0)
        if current_state in visited:
            continue
        visited.add(current_state)
        if current_state == goal_state:
            shortest_distance = distance
            break
        i, j = current_state
        if len(grid) > i - 1 >= 0 and ord(grid[i][j]) + 1 >= ord(grid[i - 1][j]):
            queue.append(((i - 1, j), distance + 1))
        if len(grid) > i + 1 >= 0 and ord(grid[i][j]) + 1 >= ord(grid[i + 1][j]):
            queue.append(((i + 1, j), distance + 1))
        if len(grid[0]) > j - 1 >= 0 and ord(grid[i][j]) + 1 >= ord(grid[i][j - 1]):
            queue.append(((i, j - 1), distance + 1))
        if len(grid[0]) > j + 1 >= 0 and ord(grid[i][j]) + 1 >= ord(grid[i][j + 1]):
            queue.append(((i, j + 1), distance + 1))
    print(shortest_distance)
