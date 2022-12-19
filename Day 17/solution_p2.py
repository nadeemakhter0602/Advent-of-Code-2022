import time


def move(rock, direction, occupied, floor=0):
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


def check_for_cycle(curr_surface_profile, rock, rounds, surface_profiles, rock_num_to_height, target_rock_num):
    if len(curr_surface_profile) < 10:
        curr_surface_profile.append(rock)
    else:
        curr_surface_profile.pop(0)
        curr_surface_profile.append(rock)
    if len(curr_surface_profile) == 10:
        curr_surface_profile = [tuple([x for x, y in layer])
                                for layer in curr_surface_profile]
        curr_surface_profile = tuple(curr_surface_profile)
        if curr_surface_profile in surface_profiles:
            prev_rock_num, prev_height = surface_profiles[curr_surface_profile]
            rock_num = rounds + 1
            cycle_height = height - prev_height
            rocks_remaining = target_rock_num - rock_num
            period = rock_num - prev_rock_num
            cycles_remaining = rocks_remaining // period
            close_to_top_rocks = target_rock_num - (rocks_remaining % period)
            rock_difference = target_rock_num - close_to_top_rocks
            top_of_target_rock = prev_rock_num + rock_difference + 1
            top_of_target_rock_height = rock_num_to_height[top_of_target_rock]
            bottom_of_target_rock = rock_num_to_height[prev_rock_num + 1]
            height_difference = top_of_target_rock_height - bottom_of_target_rock
            height_to_top = height + (cycle_height * cycles_remaining)
            final_result = height_to_top + height_difference
            print('Height of tower at', target_rock_num, 'rocks :', final_result)
            return True
        else:
            surface_profiles[curr_surface_profile] = (rounds + 1, height)
            curr_surface_profile = []
    return False


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
    surface_profiles = dict()
    rock_num_to_height = dict()
    curr_surface_profile = []
    target_rock_num = 1000000000000
    while rounds < target_rock_num:
        rock_num_to_height[rounds + 1] = height
        rock = rock_coordinates[rounds % 5]
        rock = [(x, y + height) for x, y in rock]
        result = simulate_tetris(rock, sub_round, jetstream, occupied, n)
        rock, sub_round = result
        height = max(height, rock[0][1] + 1)
        if check_for_cycle(curr_surface_profile, rock, rounds, surface_profiles, rock_num_to_height, target_rock_num):
            break
        rounds += 1
    print('Time taken :', time.time() - start)
