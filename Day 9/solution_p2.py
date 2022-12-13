def move_follower(head, follower):
    distance = ((head[0] - follower[0]) ** 2 +
                (head[1] - follower[1]) ** 2) ** 0.5
    if distance >= 2:
        if head[0] == follower[0]:
            if head[1] < follower[1]:
                follower = (follower[0], follower[1] - 1)
            else:
                follower = (follower[0], follower[1] + 1)
        elif head[1] == follower[1]:
            if head[0] < follower[0]:
                follower = (follower[0] - 1, follower[1])
            else:
                follower = (follower[0] + 1, follower[1])
        elif head[0] != follower[0] and head[1] != follower[1]:
            if head[0] > follower[0]:
                if head[1] > follower[1]:
                    follower = (follower[0] + 1, follower[1] + 1)
                else:
                    follower = (follower[0] + 1, follower[1] - 1)
            else:
                if head[1] > follower[1]:
                    follower = (follower[0] - 1, follower[1] + 1)
                else:
                    follower = (follower[0] - 1, follower[1] - 1)
    return follower


with open('input.txt') as f:
    body = [(0, 0) for i in range(10)]
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
            body[0] = (body[0][0] + movement[0], body[0][1] + movement[1])
            for i in range(len(body) - 1):
                body[i + 1] = move_follower(body[i], body[i + 1])
            visited.add(body[-1])
    print(len(visited))
