import ast


def check_order(left, right):
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if isinstance(left[l], int) and isinstance(right[r], int):
            if left[l] < right[r]:
                return True
            elif left[l] > right[r]:
                return False
        elif isinstance(left[l], list) and isinstance(right[r], list):
            result = check_order(left[l], right[r])
            if result is not None:
                return result
        elif isinstance(left[l], int) and isinstance(right[r], list):
            left[l] = [left[l]]
            result = check_order(left[l], right[r])
            if result is not None:
                return result
        elif isinstance(left[l], list) and isinstance(right[r], int):
            right[r] = [right[r]]
            result = check_order(left[l], right[r])
            if result is not None:
                return result
        l += 1
        r += 1
    if l >= len(left):
        return True
    elif r >= len(right):
        return False


with open('input.txt') as f:
    idx = 1
    sum_idx = 0
    for pair in f.read().split('\n\n'):
        left, right = pair.split('\n')
        left = ast.literal_eval(left)
        right = ast.literal_eval(right)
        if check_order(left, right):
            sum_idx += idx
        idx += 1
    print(sum_idx)
