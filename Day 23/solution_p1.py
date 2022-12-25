import time


def first_half(elf_coordinates, elf_coordinates_set, directions, offsets):
    proposed_coordinates = []
    for elf in elf_coordinates:
        has_elf = False
        # considering 8 adjacent positions
        for offset in offsets:
            offset = offsets[offset]
            pos = (elf[0] + offset[0], elf[1] + offset[1])
            if pos in elf_coordinates_set:
                has_elf = True
                break
        # any of the 8 positions has an elf
        if has_elf:
            for direction_set in directions:
                no_elf = True
                # check 3 directions in the direction set
                for direction in direction_set:
                    offset = offsets[direction]
                    pos = (elf[0] + offset[0], elf[1] + offset[1])
                    if pos in elf_coordinates_set:
                        no_elf = False
                        break
                # if there is no elf in 3 directions
                if no_elf:
                    offset = offsets[direction_set[0]]
                    pos = (elf[0] + offset[0], elf[1] + offset[1])
                    proposed_coordinates.append(pos)
                    break
            # if elf exists in all 4 directions
            if not no_elf:
                proposed_coordinates.append(None)
        # any of the 8 positions do not have an elf
        else:
            proposed_coordinates.append(None)
    return proposed_coordinates


def second_half(proposed_coordinates, elf_coordinates):
    for i in range(len(elf_coordinates)):
        if proposed_coordinates[i] is not None:
            if proposed_coordinates[i] not in proposed_coordinates[i + 1:]:
                if proposed_coordinates[i] not in proposed_coordinates[:i]:
                    elf_coordinates[i] = proposed_coordinates[i]


with open('input.txt') as f:
    start = time.time()
    ground = [i for i in f.read().split('\n')]
    offsets = {'N': (-1, 0),
               'NE': (-1, 1),
               'NW': (-1, -1),
               'S': (1, 0),
               'SE': (1, 1),
               'SW': (1, -1),
               'W': (0, -1),
               'E': (0, 1)}
    directions = [['N', 'NE', 'NW'],
                  ['S', 'SE', 'SW'],
                  ['W', 'NW', 'SW'],
                  ['E', 'NE', 'SE']]
    elf_coordinates = []
    for row in range(len(ground)):
        for col in range(len(ground[0])):
            if ground[row][col] == '#':
                elf_coordinates.append((row, col))
    elf_coordinates_set = set(elf_coordinates)
    rounds = 0
    while rounds < 10:
        proposed_coordinates = first_half(elf_coordinates,
                                          elf_coordinates_set,
                                          directions,
                                          offsets)
        second_half(proposed_coordinates, elf_coordinates)
        elf_coordinates_set = set(elf_coordinates)
        first_direction = directions.pop(0)
        directions.append(first_direction)
        rounds += 1
    row_start = min([i[0] for i in elf_coordinates])
    row_end = max([i[0] for i in elf_coordinates])
    col_start = min([i[1] for i in elf_coordinates])
    col_end = max([i[1] for i in elf_coordinates])
    row_size = row_end - row_start + 1
    col_size = col_end - col_start + 1
    empty_ground = row_size * col_size - len(elf_coordinates)
    print('Number of empty ground tiles :', empty_ground)
    print('Time taken :', time.time() - start)
