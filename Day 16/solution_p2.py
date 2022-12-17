from functools import lru_cache
import time


def parse(line):
    line = line.split(';')
    valve = line[0][6:8]
    flow_rate = int(line[0][23:])
    valves = list(map(str.strip, line[1][23:].split(',')))
    return valve, flow_rate, valves


@lru_cache(maxsize=None)
def dfs(valve, time, visited, players):
    if time <= 1:
        if players > 0:
            return dfs('AA', 26, visited, players - 1)
        else:
            return 0
    res = 0
    for node in graph[valve]:
        res = max(res, dfs(node, time - 1, visited, players))
    if valve not in visited and flow_rates[valve] > 0:
        visited = tuple(sorted([*visited, valve]))
        res = max(res, dfs(valve, time - 1, visited, players) + flow_rates[valve] * (time - 1))
    return res


with open('input.txt') as f:
    graph = dict()
    flow_rates = dict()
    for line in f.read().split('\n'):
        valve, flow_rate, valves = parse(line)
        graph[valve] = valves
        flow_rates[valve] = flow_rate
    start = time.time()
    print('Solution :', dfs('AA', 26, (), 1))
    print('Time taken :', time.time() - start)
