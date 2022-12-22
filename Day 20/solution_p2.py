import time


with open('input.txt') as f:
    start = time.time()
    ciphertext = []
    processed = set()
    decryption_key = 811589153
    text = list(map(int, f.read().split('\n')))
    for i in text:
        i = (i * decryption_key, 0)
        while i in processed:
            i = (i[0], i[1] + 1)
        if i not in processed:
            ciphertext.append(i)
        processed.add(i)
    n = len(ciphertext)
    plaintext = ciphertext.copy()
    for _ in range(10):
        for i in range(n):
            num = ciphertext[i]
            pos1 = plaintext.index(num)
            plaintext.pop(pos1)
            pos2 = (num[0] + pos1) % len(plaintext)
            plaintext.insert(pos2, num)
    pos_0 = plaintext.index((0, 0))
    groove_coordinates = []
    sum_groove_coordinates = 0
    for i in (1000, 2000, 3000):
        pos = (i + pos_0) % n
        coordinate = plaintext[pos][0]
        groove_coordinates.append(coordinate)
        sum_groove_coordinates += coordinate
    print('Groove coordinates :', groove_coordinates)
    print('Sum of groove coordinates :', sum_groove_coordinates)
    print('Time taken :', time.time() - start)
