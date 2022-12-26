import time


def SNAFU_to_decimal(number, digits):
    decimal = 0
    for i in range(len(number)):
        decimal += (5**i) * digits[number[-(i + 1)]]
    return decimal


def decimal_to_SNAFU(number, digits):
    pentinary = ''
    while number != 0:
        rem = number % 5
        pentinary = str(rem) + pentinary
        number = number // 5
    snafu = ''
    carry = 0
    digit = 0
    for i in range(len(pentinary)):
        if digit > 2:
            digit -= 5
            carry = 1
        else:
            carry = 0
        snafu = digits[digit] + snafu
        digit = int(pentinary[-(i + 1)]) + carry
    if digit > 2:
        digit -= 5
        carry = 1
    else:
        carry = 0
    snafu = digits[digit] + snafu
    digit = int(pentinary[-(i + 1)]) + carry
    if carry == 1:
        snafu = '1' + snafu
    return snafu[:-1]


with open('input.txt') as f:
    start = time.time()
    digits = {'-': -1,
              '=': -2,
              '2': 2,
              '1': 1,
              '0': 0,
              -1: '-',
              -2: '=',
              2: '2',
              1: '1',
              0: '0'}
    numbers = f.read().split('\n')
    sum_numbers = 0
    for number in numbers:
        sum_numbers += SNAFU_to_decimal(number, digits)
    print('SNAFU number to supply :', decimal_to_SNAFU(sum_numbers, digits))
    print('Time taken :', time.time() - start)
