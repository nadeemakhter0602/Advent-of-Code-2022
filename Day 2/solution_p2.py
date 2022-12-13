outcome = {'X': 0, 'Y': 3, 'Z': 6}
shape = {'A': 1, 'B': 2, 'C': 3}
choice = {'A X': 'C', 'B Y': 'B', 'C Z': 'A', 'A Y': 'A',
          'A Z': 'B', 'B X': 'A', 'B Z': 'C', 'C X': 'B', 'C Y': 'C'}
total = 0
with open('input.txt') as f:
    for i in f.read().split('\n'):
        total += outcome[i[-1]] + shape[choice[i]]
    print(total)
