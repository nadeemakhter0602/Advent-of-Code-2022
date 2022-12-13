with open('input.txt') as f:
    X = 1
    cycle = 0
    y = 0
    for line in f.read().split('\n'):
        line = line.split(' ')
        op = line[0]
        sprite = [X - 1, X, X + 1]
        if op == 'noop':
            cycle += 1
            y = (cycle - 1) % 40
            if y in sprite:
                print('#', end='')
            else:
                print('.', end='')
            if cycle % 40 == 0:
                print()
                y += 1
        elif op == 'addx':
            for i in range(2):
                cycle += 1
                y = (cycle - 1) % 40
                if y in sprite:
                    print('#', end='')
                else:
                    print('.', end='')
                if cycle % 40 == 0:
                    print()
                    y += 1
            X += int(line[1])
