import time


def parse(line, last_bottom):
    coordinates = []
    current_bottom = 0
    line = line.split(' -> ')
    for coordinate in line:
        coordinate = list(map(int, coordinate.split(',')))
        last_bottom = max(coordinate[1], last_bottom)
        coordinates.append(coordinate)
    return coordinates, last_bottom


def find_rocks(coordinates, rocks):
    for i in range(len(coordinates) - 1):
        left = coordinates[i]
        right = coordinates[i + 1]
        if left[0] < right[0]:
            for j in range(left[0], right[0] + 1):
                rocks.add((j, left[1]))
        elif left[1] < right[1]:
            for j in range(left[1], right[1] + 1):
                rocks.add((left[0], j))
        elif left[0] > right[0]:
            for j in range(right[0], left[0] + 1):
                rocks.add((j, left[1]))
        elif left[1] > right[1]:
            for j in range(right[1], left[1] + 1):
                rocks.add((left[0], j))


def traverse(rocks, resting_sand_units, sand_source, last_bottom):
    stack = [sand_source]
    memo = dict()
    while len(stack) > 0:
        i, j = stack.pop()
        if j == last_bottom:
            return
        down = (i, j + 1)
        diagonal_right = (i + 1, j + 1)
        diagonal_left = (i - 1, j + 1)
        if down not in rocks and down not in resting_sand_units:
            memo[down] = (i, j)
            stack.append(down)
        elif diagonal_left not in rocks and diagonal_left not in resting_sand_units:
            memo[diagonal_left] = (i, j)
            stack.append(diagonal_left)
        elif diagonal_right not in rocks and diagonal_right not in resting_sand_units:
            memo[diagonal_right] = (i, j)
            stack.append(diagonal_right)
        else:
            resting_sand_units.add((i, j))
            stack = [memo[(i, j)]]


with open('input.txt') as f:
    sand_source = (500, 0)
    rocks = set()
    resting_sand_units = set()
    last_bottom = 0
    for line in f.read().split('\n'):
        coordinates, current_bottom = parse(line, last_bottom)
        last_bottom = max(last_bottom, current_bottom)
        find_rocks(coordinates, rocks)
    start = time.time()
    traverse(rocks, resting_sand_units, sand_source, last_bottom)
    print('Units of sand :', len(resting_sand_units))
    print('Time taken :', time.time() - start)
