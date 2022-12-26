import time


def find_blizzard_positions(blizzard_positions, row_end, col_end):
    blizzard_positions_in_time = dict()
    for time in range(0, col_end * row_end * 3):
        occupied = set()
        for i in range(len(blizzard_positions)):
            row, col, direction = blizzard_positions[i]
            if direction == '>':
                col += 1
                if col > col_end:
                    col = 1
            elif direction == '<':
                col -= 1
                if col < 1:
                    col = col_end
            elif direction == '^':
                row -= 1
                if row < 1:
                    row = row_end
            elif direction == 'v':
                row += 1
                if row > row_end:
                    row = 1
            blizzard_positions[i] = (row, col, direction)
            occupied.add((row, col))
        blizzard_positions_in_time[time] = occupied
    return blizzard_positions_in_time


def traverse(curr, goal, time, blizzard_positions_in_time, row_end, col_end, visited):
    queue = [(curr, time)]
    min_time = float('inf')
    while len(queue) > 0:
        curr, time = queue.pop(0)
        if curr == goal:
            min_time = min(time, min_time)
            break
        if (curr, time) in visited:
            continue
        if not ((1 <= curr[0] <= row_end and 1 <= curr[1] <= col_end) or curr == (row_end + 1, col_end) or curr == (0, 1)):
            continue
        visited.add((curr, time))
        occupied = blizzard_positions_in_time[time]
        # move up
        if (curr[0] - 1, curr[1]) not in occupied:
            queue.append(((curr[0] - 1, curr[1]), time + 1))
        # move down
        if (curr[0] + 1, curr[1]) not in occupied:
            queue.append(((curr[0] + 1, curr[1]), time + 1))
        # move left
        if (curr[0], curr[1] - 1) not in occupied:
            queue.append(((curr[0], curr[1] - 1), time + 1))
        # move right
        if (curr[0], curr[1] + 1) not in occupied:
            queue.append(((curr[0], curr[1] + 1), time + 1))
        # wait
        if curr not in occupied:
            queue.append((curr, time + 1))
    return min_time


with open('input.txt') as f:
    start_time = time.time()
    valley = [line for line in f.read().split('\n')]
    start = (0, 1)
    goal = (len(valley) - 1, len(valley[0]) - 2)
    row_end = len(valley) - 2
    col_end = len(valley[0]) - 2
    blizzard_positions = []
    for i in range(len(valley)):
        for j in range(len(valley[0])):
            if valley[i][j] in ['>', '^', '<', 'v']:
                blizzard_positions.append((i, j, valley[i][j]))
    blizzard_positions_in_time = find_blizzard_positions(blizzard_positions,
                                                         row_end,
                                                         col_end)
    time1 = traverse(start, goal, 0, blizzard_positions_in_time,
                     row_end, col_end, set())
    time2 = traverse(goal, start, time1, blizzard_positions_in_time,
                     row_end, col_end, set())
    time3 = traverse(start, goal, time2, blizzard_positions_in_time,
                     row_end, col_end, set())
    print('Fewest minutes required to perform trip :', time3)
    print('Time taken :', time.time() - start_time)
