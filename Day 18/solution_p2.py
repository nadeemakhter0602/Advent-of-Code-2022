import time


def flood_fill(node, nodes, min_max_coordinates, offsets, visited):
    stack = [node]
    min_x, min_y, min_z, max_x, max_y, max_z = min_max_coordinates
    while stack != []:
        node = stack.pop()
        x1, y1, z1 = node
        if not (min_x <= x1 <= max_x and min_y <= y1 <= max_y and min_z <= z1 <= max_z):
            continue
        if node in visited:
            continue
        if node in nodes:
            continue
        visited.add(node)
        for offset in offsets:
            x2, y2, z2 = offset
            x, y, z = (x1 + x2, y1 + y2, z1 + z2)
            stack.append((x, y, z))


with open('input.txt') as f:
    start = time.time()
    coordinates = set()
    offsets = [(0, 0, 1),
               (0, 0, -1),
               (0, 1, 0),
               (0, -1, 0),
               (1, 0, 0),
               (-1, 0, 0)]
    max_x = float('-inf')
    min_x = float('inf')
    max_y = float('-inf')
    min_y = float('inf')
    max_z = float('-inf')
    min_z = float('inf')
    for line in f.read().split('\n'):
        x, y, z = list(map(int, line.split(',')))
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        max_z = max(max_z, z)
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        min_z = min(min_z, z)
        coordinates.add((x, y, z))
    visited = set()
    lowest_point = (min_x - 1, min_y - 1, min_z - 1)
    highest_point = (max_x + 1, max_y + 1, max_z + 1)
    min_max_coordinates = (*lowest_point, *highest_point)
    flood_fill(lowest_point, coordinates,
               min_max_coordinates, offsets, visited)
    exposed_edges = 0
    for coordinate in list(coordinates):
        x1, y1, z1 = coordinate
        for offset in offsets:
            x2, y2, z2 = offset
            x, y, z = (x1 + x2, y1 + y2, z1 + z2)
            if (x, y, z) in visited:
                exposed_edges += 1
    print('Number of exposed edges :', exposed_edges)
    print('Time taken :', time.time() - start)
