import time


def parse(line):
    line = line.split(':')
    sensor = line[0]
    beacon = line[1]
    sensor = sensor[10:].split(',')
    beacon = beacon[22:].split(',')
    sensor = (int(sensor[0][2:]), int(sensor[1][3:]))
    beacon = (int(beacon[0][2:]), int(beacon[1][3:]))
    return sensor, beacon


def get_manhattan_distance(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])


def generate_manhattan_square(sensor, beacon, y):
    manhattan_distance = get_manhattan_distance(sensor, beacon)
    y_distance = abs(sensor[1] - y)
    if y_distance <= manhattan_distance:
        x_distance = manhattan_distance - y_distance
        left = sensor[0] - x_distance
        right = sensor[0] + x_distance
        return left, right


def find_gaps(ranges):
    gaps = []
    last_covered_point = ranges[0][1]
    for interval in ranges:
        start = interval[0]
        end = interval[1]
        if start > last_covered_point + 1:
            gaps.append([last_covered_point + 1, start - 1])
        last_covered_point = max(last_covered_point, end)
    return gaps


with open('input.txt') as f:
    start = time.time()
    beacon_position = None
    sensors_and_beacons = list()
    for line in f.read().split('\n'):
        sensor, beacon = parse(line)
        sensors_and_beacons.append((sensor, beacon))
    for y in range(0, 4000001):
        ranges = []
        for sensor, beacon in sensors_and_beacons:
            result = generate_manhattan_square(sensor, beacon, y)
            if result is not None:
                left, right = result
                left = max(0, left)
                right = min(4000000, right)
                ranges.append((left, right))
        ranges.sort(key=lambda x: x[0])
        gaps = find_gaps(ranges)
        if len(gaps) > 0:
            beacon_position = (gaps[0][0], y)
            break
    print('Only possible position for the distress beacon :', beacon_position)
    print('Tuning frequency :', beacon_position[0] * 4000000 + beacon_position[1])
    print('Time taken :', time.time() - start)
