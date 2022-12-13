def traverse(filesystem):
    for key, value in filesystem.items():
        if isinstance(value, dict):
            for pair in traverse(value):
                yield (key, *pair)
        else:
            yield (key, value)


with open('input.txt') as f:
    directory = []
    filesystem = []
    working_dir = {'/': dict()}
    for line in f:
        line = line[:-1].split(' ')
        if line[0] == '$':
            if line[1] == 'cd':
                if line[2] == '..':
                    directory.pop()
                    working_dir = filesystem.pop()
                else:
                    directory.append(line[2])
                    filesystem.append(working_dir)
                    working_dir = working_dir[line[2]]
        else:
            if line[0] == 'dir':
                working_dir[line[1]] = dict()
            else:
                working_dir[line[1]] = int(line[0])
    filesystem = filesystem[0]
    max_depth = 0
    for i in traverse(filesystem):
        max_depth = max(max_depth, len(i))
    max_depth -= 2
    smallest_dir = float('inf')
    total_used_space = 0
    for depth in range(max_depth):
        directory_map = dict()
        for path in traverse(filesystem):
            if depth < len(path) - 2:
                if isinstance(path[depth], str):
                    key = ' '.join(path[:depth+1])
                    if key in directory_map:
                        directory_map[key] += path[-1]
                    else:
                        directory_map[key] = path[-1]
        for directory in directory_map:
            if directory == '/':
                total_used_space = directory_map[directory]
            if (30000000 - (70000000 - total_used_space)) <= directory_map[directory] <= smallest_dir:
                smallest_dir = directory_map[directory]
    print(smallest_dir)
