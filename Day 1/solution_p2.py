with open('input.txt') as f:
    lines = f.read().split('\n')
    top3 = 0
    prev_max = float('inf')
    for j in range(3):
        curr_max = 0
        total = 0
        for i in lines:
            if i == '':
                if curr_max < total < prev_max:
                    curr_max = total
                total = 0
            else:
                total += int(i)
        prev_max = curr_max
        top3 += curr_max
    print(top3)
