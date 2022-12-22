import time


def parse(line):
    line = line.split(': ')
    monkey = line[0]
    if str.isnumeric(line[1]):
        return monkey, int(line[1])
    else:
        return monkey, line[1].split(' ')


def traverse(monkey, graph):
    curr = graph[monkey]
    if isinstance(curr, int):
        return graph[monkey]
    elif curr[1] == '+':
        return traverse(curr[0], graph) + traverse(curr[2], graph)
    elif curr[1] == '*':
        return traverse(curr[0], graph) * traverse(curr[2], graph)
    elif curr[1] == '-':
        return traverse(curr[0], graph) - traverse(curr[2], graph)
    return traverse(curr[0], graph) / traverse(curr[2], graph)


with open('input.txt') as f:
    start = time.time()
    graph = dict()
    lines = f.read().split('\n')
    for line in lines:
        monkey, job = parse(line)
        graph[monkey] = job
    print('The number root yells is :', traverse('root', graph))
    print('Time taken :', time.time() - start)
