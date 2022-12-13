import ast
from functools import cmp_to_key


def check_order(left, right):
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if isinstance(left[l], int) and isinstance(right[r], int):
            if left[l] < right[r]:
                return -1
            elif left[l] > right[r]:
                return 1
        elif isinstance(left[l], list) and isinstance(right[r], list):
            result = check_order(left[l], right[r])
            if result is not None:
                return result
        elif isinstance(left[l], int) and isinstance(right[r], list):
            result = check_order([left[l]], right[r])
            if result is not None:
                return result
        elif isinstance(left[l], list) and isinstance(right[r], int):
            result = check_order(left[l], [right[r]])
            if result is not None:
                return result
        l += 1
        r += 1
    if l >= len(left):
        return -1
    elif r >= len(right):
        return 1


with open('input.txt') as f:
    idx = 1
    sum_idx = 0
    packets = []
    for pair in f.read().split('\n\n'):
        left, right = pair.split('\n')
        left = ast.literal_eval(left)
        right = ast.literal_eval(right)
        packets.append(left)
        packets.append(right)
    packets.append([[2]])
    packets.append([[6]])
    packets.sort(key=cmp_to_key(check_order))
    decoder_key = 1
    for idx in range(len(packets)):
        if packets[idx] == [[2]] or packets[idx] == [[6]]:
            decoder_key *= idx + 1
    print(decoder_key)
