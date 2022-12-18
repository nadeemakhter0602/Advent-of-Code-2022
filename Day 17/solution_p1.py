import time


def move(rock, direction, occupied):
    movement = {'down': (0, -1),
                '<': (-1, 0),
                '>': (1, 0)}
    i, j = (movement[direction][0], movement[direction][1])
    new_rock = []
    for x, y in rock:
        x = x + i
        y = y + j
        if 0 <= x <= 6 and y >= 0 and (x, y) not in occupied:
            new_rock.append((x, y))
        else:
            return rock
    return new_rock


def simulate_tetris(rock, sub_round, jetstream, occupied, n):
    while True:
        direction = jetstream[sub_round % n]
        sub_round += 1
        rock = move(rock, direction, occupied)
        rock_down = move(rock, 'down', occupied)
        if rock == rock_down:
            break
        else:
            rock = rock_down
    for coordinates in rock:
        occupied.add(coordinates)
    return rock, sub_round


with open('input.txt') as f:
    start = time.time()
    jetstream = []
    for movement in f.read():
        jetstream.append(movement)
    n = len(jetstream)
    occupied = set()
    rock_coordinates = {0: [(2, 3), (3, 3), (4, 3), (5, 3)],
                        1: [(3, 5), (2, 4), (3, 4), (4, 4), (3, 3)],
                        2: [(4, 5), (4, 4), (2, 3), (3, 3), (4, 3)],
                        3: [(2, 6), (2, 5), (2, 4), (2, 3)],
                        4: [(2, 4), (3, 4), (2, 3), (3, 3)]}
    rounds = 0
    height = 0
    sub_round = 0
    while rounds < 2022:
        rock = rock_coordinates[rounds % 5]
        rock = [(x, y + height) for x, y in rock]
        result = simulate_tetris(rock, sub_round, jetstream, occupied, n)
        rock, sub_round = result
        height = max(height, rock[0][1] + 1)
        rounds += 1
    print('Height of tower of rocks :', height)
    print('Time taken :', time.time() - start)
