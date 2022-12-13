with open('input.txt') as f:
    total = 0
    m = 0
    for i in f.read().split('\n'):
        if i == '':
            if total > m:
                m = total
            total = 0
        else:
            total += int(i)
    print(m)
