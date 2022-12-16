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


def generate_manhattan_square(sensor, beacon, y, no_beacon_positions):
    mh_distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    y_distance = abs(sensor[1] - y)
    if y_distance <= mh_distance:
        x_distance = mh_distance - y_distance
        left = sensor[0]
        right = sensor[0]
        while right <= sensor[0] + x_distance:
            no_beacon_positions.add((left, y))
            no_beacon_positions.add((right, y))
            left -= 1
            right += 1
    no_beacon_positions.discard(beacon)


with open('input.txt') as f:
    start = time.time()
    y = 2000000
    no_beacon_positions = set()
    for line in f.read().split('\n'):
        sensor, beacon = parse(line)
        print('Checking for sensor', sensor, 'and beacon', beacon)
        generate_manhattan_square(sensor, beacon, y, no_beacon_positions)
    print('Number of positions with no beacons :', len(no_beacon_positions))
    print('Time taken :', time.time() - start)
