from functools import lru_cache
import time


def parse(line):
    line = line.split(';')
    valve = line[0][6:8]
    flow_rate = int(line[0][23:])
    valves = list(map(str.strip, line[1][23:].split(',')))
    return valve, flow_rate, valves


@lru_cache(maxsize=None)
def dfs(valve, time, visited=()):
    if time <= 1:
        return 0
    res = 0
    for node in graph[valve]:
        res = max(res, dfs(node, time - 1, visited))
    if valve not in visited and flow_rates[valve] > 0:
        visited = tuple(sorted([*visited, valve]))
        res = max(res, dfs(valve, time - 1, visited) + flow_rates[valve] * (time - 1))
    return res


with open('input.txt') as f:
    graph = dict()
    flow_rates = dict()
    for line in f.read().split('\n'):
        valve, flow_rate, valves = parse(line)
        graph[valve] = valves
        flow_rates[valve] = flow_rate
    start = time.time()
    print('Solution :', dfs('AA', 30))
    print('Time taken :', time.time() - start)
