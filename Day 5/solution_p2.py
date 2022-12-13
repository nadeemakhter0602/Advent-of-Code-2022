with open('input.txt') as f:
    towers = {1: [i for i in 'RNFVLJSM'],
              2: [i for i in 'PNDZFJWH'],
              3: [i for i in 'WRCDG'],
              4: [i for i in 'NBS'],
              5: [i for i in 'MZWPCBFN'],
              6: [i for i in 'PRMW'],
              7: [i for i in 'RTNGLSW'],
              8: [i for i in 'QTHFNBV'],
              9: [i for i in 'LMHZNF']}
    skip = True
    for line in f.read().split('\n'):
        if line != '' and skip:
            continue
        elif line == '':
            skip = False
            continue
        line = line.split(' ')
        crates, from_tower, to_tower = int(line[1]), int(line[3]), int(line[5])
        stack = []
        while crates > 0:
            stack.append(towers[from_tower].pop())
            crates -= 1
        while stack != []:
            towers[to_tower].append(stack.pop())
    message = ''
    for i in towers:
        message += towers[i].pop()
    print(message)
