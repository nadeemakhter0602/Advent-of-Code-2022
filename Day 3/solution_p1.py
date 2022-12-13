with open('input.txt') as f:
    priorities = {}
    priority = 1
    for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        priorities[i] = priority
        priority += 1
    priority = 0
    for line in f.read().split():
        l = len(line)
        compt1 = set(line[:l//2])
        compt2 = set(line[l//2:])
        common = compt1.intersection(compt2)
        for item in common:
            priority += priorities[item]
    print(priority)
