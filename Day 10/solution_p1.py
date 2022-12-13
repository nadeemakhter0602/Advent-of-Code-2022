with open('input.txt') as f:
    X = 1
    cycle = 0
    signal_strength = 0
    for line in f.read().split('\n'):
        line = line.split(' ')
        op = line[0]
        if op == 'noop':
            cycle += 1
            if (cycle - 20) % 40 == 0:
                signal_strength += (cycle * X)
        elif op == 'addx':
            for i in range(2):
                cycle += 1
                if (cycle - 20) % 40 == 0:
                    signal_strength += (cycle * X)
            X += int(line[1])
    print(signal_strength)
