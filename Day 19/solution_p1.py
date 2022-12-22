import time


def parse(line, blueprints):
    line = line.split(':')
    number = int(line[0][10:])
    line = line[1]
    line = line.split('.')
    ore_robot = line[0]
    clay_robot = line[1]
    obsidian_robot = line[2]
    geode_robot = line[3]
    ore_robot = int(ore_robot[21:-4])
    clay_robot = int(clay_robot[22:-4])
    obsidian_robot = obsidian_robot[26:].split(' ore and ')
    obsidian_robot = (int(obsidian_robot[0]), int(obsidian_robot[1][:-5]))
    geode_robot = geode_robot[23:].split(' ore and ')
    geode_robot = (int(geode_robot[0]), int(geode_robot[1][:-9]))
    return (ore_robot, clay_robot, obsidian_robot, geode_robot)


def max_geodes_every_minute(time, geode_robots=0, geode=0):
    if time == 0:
        return geode
    # build geode robot each minute
    geode += geode_robots
    geode_robots += 1
    return max_geodes_every_minute(time - 1, geode_robots, geode)


def traverse(blueprint, time, robots, materials, geode, cache):
    state = (time, robots, materials)
    if state in cache:
        return cache[state]
    if time == 0:
        return materials[3]
    max_geode_possible = materials[3] + \
        (robots[3] * time) + max_geodes_every_minute(time)
    if geode > max_geode_possible:
        return geode
    max_ore = max([blueprint[0], blueprint[1],
                  blueprint[2][0], blueprint[3][0]])
    max_clay = blueprint[2][1]
    max_obsidian = blueprint[3][1]
    # one minute to get each material per robot
    geode = max(geode,
                traverse(blueprint, time - 1, robots,
                         (materials[0] + robots[0], materials[1] + robots[1],
                          materials[2] + robots[2], materials[3] + robots[3]),
                         geode, cache))
    # check if you have enough materials to build ore robot
    if materials[0] >= blueprint[0] and robots[0] < max_ore:
        # build ore robot and each robot gets materials
        geode = max(geode,
                    traverse(blueprint, time - 1,
                             (robots[0] + 1, robots[1], robots[2], robots[3]),
                             (materials[0] - blueprint[0] + robots[0],
                              materials[1] + robots[1],
                              materials[2] + robots[2],
                              materials[3] + robots[3]),
                             geode, cache))
    # check if you have enough materials to build clay robot
    if materials[0] >= blueprint[1] and robots[1] < max_clay:
        # build clay robot and each robot gets materials
        geode = max(geode,
                    traverse(blueprint, time - 1,
                             (robots[0], robots[1] + 1, robots[2], robots[3]),
                             (materials[0] - blueprint[1] + robots[0],
                              materials[1] + robots[1],
                              materials[2] + robots[2],
                              materials[3] + robots[3]),
                             geode, cache))
    # check if you have enough materials to build obsidian robot
    if materials[0] >= blueprint[2][0] and materials[1] >= blueprint[2][1] and robots[2] < max_obsidian:
        # build obsidian robot and each robot gets materials
        geode = max(geode,
                    traverse(blueprint, time - 1,
                             (robots[0], robots[1], robots[2] + 1, robots[3]),
                             (materials[0] - blueprint[2][0] + robots[0],
                                 materials[1] - blueprint[2][1] + robots[1],
                                 materials[2] + robots[2], materials[3] + robots[3]),
                             geode, cache))
    # check if you have enough materials to build geode robot
    if materials[0] >= blueprint[3][0] and materials[2] >= blueprint[3][1]:
        # build geode robot and each robot gets materials
        geode = max(geode,
                    traverse(blueprint, time - 1,
                             (robots[0], robots[1], robots[2], robots[3] + 1),
                             (materials[0] - blueprint[3][0] + robots[0], materials[1] + robots[1],
                              materials[2] - blueprint[3][1] + robots[2], materials[3] + robots[3]),
                             geode, cache))
    cache[state] = geode
    return geode


'''
    We have geode cracking robots, obsidian collecting robots, clay collecting robots,
    and ore collecting robots.
    Each robot only collects one of its resource per minute.
    Robot factory takes a minute to make robots.
    You start with one ore collecting robot.
    ore collecting robot => collect ore => make clay collecting robot
    clay collecting robot => collect clay => make obsidian collecting robot (uses both clay and ore)
    obsidian collecting robot => collect obsidian => make geode cracking robots (uses both obsidian and ore)
    geode cracking robots => collect geode
    24 minutes to max out geode
'''
with open('input.txt') as f:
    start = time.time()
    blueprints = []
    robots = (1, 0, 0, 0)
    materials = (0, 0, 0, 0)
    quality_level_sum = 0
    for line in f.read().split('\n'):
        blueprints.append(parse(line, blueprints))
    for i in range(len(blueprints)):
        print('Blueprint', i + 1)
        quality_level_sum += traverse(blueprints[i],
                                      24, robots, materials, 0, dict()) * (i + 1)
    print('Sum of quality levels :', quality_level_sum)
    print('Time taken : ', time.time() - start)
