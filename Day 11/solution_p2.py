with open('input.txt') as f:
    instructions = dict()
    inspect_map = dict()
    base = 1

    for note in f.read().split('\n\n'):
        line = note.split('\n')
        monkey = line[0][-2]
        items = line[1][18:]
        items = list(map(int, items.split(',')))
        expression = line[2][19:]
        expression = expression.split(' ')
        divisor = int(line[3].split(' ')[-1])
        base *= divisor
        next_monkey_true = line[4][-1]
        next_monkey_false = line[5][-1]
        inspect_map[monkey] = 0
        instructions[monkey] = {'items': items,
                                'expression': expression,
                                'divisor': divisor,
                                True: next_monkey_true,
                                False: next_monkey_false}

    for i in range(10000):
        for monkey in instructions:
            instruction = instructions[monkey]
            items = instruction['items']
            expression = instruction['expression']
            divisor = instruction['divisor']
            while len(items) > 0:
                inspect_map[monkey] += 1
                item = items.pop()
                new_worry_level = 0
                a = item if expression[0] == 'old' else int(expression[0])
                b = item if expression[2] == 'old' else int(expression[2])
                if expression[1] == '*':
                    new_worry_level = (a * b) % base
                else:
                    new_worry_level = (a + b) % base
                next_monkey = instruction[new_worry_level % divisor == 0]
                instructions[next_monkey]['items'].append(new_worry_level)

    top2 = []
    previous_max = float('inf')
    for i in range(2):
        current_max = 0
        for monkey in inspect_map:
            if previous_max > inspect_map[monkey] > current_max:
                current_max = inspect_map[monkey]
        top2.append(current_max)
        previous_max = current_max
    print(top2[0] * top2[1])
