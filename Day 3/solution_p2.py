class UniversalSet():

    def intersection(self, other):
        return other


with open('input.txt') as f:
    priorities = {}
    priority = 1
    for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        priorities[i] = priority
        priority += 1
    count = 1
    priority = 0
    common = UniversalSet()
    for line in f.read().split():
        line = set(line)
        common = common.intersection(line)
        if count % 3 == 0:
            priority += priorities[common.pop()]
            common = UniversalSet()
        count += 1
    print(priority)
