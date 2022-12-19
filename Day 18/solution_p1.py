import time


with open('input.txt') as f:
    start = time.time()
    coordinates = set()
    offsets = [(0, 0, 1),
               (0, 0, -1),
               (0, 1, 0),
               (0, -1, 0),
               (1, 0, 0),
               (-1, 0, 0)]
    for line in f.read().split('\n'):
        x, y, z = list(map(int, line.split(',')))
        coordinates.add((x, y, z))
    total_edges = len(coordinates) * 6
    for coordinate in list(coordinates):
        x1, y1, z1 = coordinate
        for offset in offsets:
            x2, y2, z2 = offset
            if (x1 + x2, y1 + y2, z1 + z2) in coordinates:
                total_edges -= 1
    print('Number of exposed edges :', total_edges)
    print('Time taken :', time.time() - start)
