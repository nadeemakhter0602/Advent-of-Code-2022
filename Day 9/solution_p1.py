with open('input.txt') as f:
    head = (0, 0)
    tail = (0, 0)
    prev_head_pos = (0, 0)
    visited = {(0, 0)}
    movement_map = {'R': (1, 0),
                    'L': (-1, 0),
                    'U': (0, 1),
                    'D': (0, -1)}
    for line in f.read().split('\n'):
        line = line.split(' ')
        steps = int(line[1])
        for i in range(steps):
            movement = movement_map[line[0]]
            head = (head[0] + movement[0], head[1] + movement[1])
            distance = ((head[0] - tail[0]) ** 2 +
                        (head[1] - tail[1]) ** 2) ** 0.5
            if distance >= 2:
                tail = (prev_head_pos[0], prev_head_pos[1])
                visited.add(tail)
            prev_head_pos = (head[0], head[1])
    print(len(visited))
