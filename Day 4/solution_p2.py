with open('input.txt') as f:
    count = 0
    for line in f.read().split('\n'):
        ranges = line.split(',')
        range1 = ranges[0].split('-')
        range2 = ranges[1].split('-')
        if int(range1[1]) >= int(range2[0]) and int(range1[0]) <= int(range2[1]):
            count += 1
        elif int(range1[1]) >= int(range2[0]) and int(range1[0]) <= int(range2[1]):
            count += 1
    print(count)
