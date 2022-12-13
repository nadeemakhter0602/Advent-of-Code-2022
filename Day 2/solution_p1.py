shape = {'X': 1, 'Y': 2, 'Z': 3}
outcome = {'A X': 3, 'B Y': 3, 'C Z': 3, 'A Y': 6,
           'A Z': 0, 'B X': 0, 'B Z': 6, 'C X': 6, 'C Y': 0}
total = 0
with open('input.txt') as f:
    for i in f.read().split('\n'):
        total += outcome[i] + shape[i[-1]]
    print(total)
