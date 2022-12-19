import time


with open('input.txt') as f:
    start = time.time()
    coordinates = []
    for line in f.read().split('\n'):
        x, y, z = list(map(int, line.split(',')))
        coordinates.append((x, y, z))
    total_edges = len(coordinates) * 6
    for i in range(len(coordinates)):
        for j in range(len(coordinates)):
            if i != j:
                x1, y1, z1 = coordinates[i]
                x2, y2, z2 = coordinates[j]
                adjacency = abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)
                if adjacency == 1:
                    total_edges -= 1
    print('Number of exposed edges :', total_edges)
    print('Time taken :', time.time() - start)
