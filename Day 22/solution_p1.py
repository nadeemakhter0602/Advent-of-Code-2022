import re
import time


def move(steps, facing, row, col, board):
    if facing == 'R':
        return move_right(steps, row, col, board)
    elif facing == 'L':
        return move_left(steps, row, col, board)
    elif facing == 'U':
        return move_up(steps, row, col, board)
    elif facing == 'D':
        return move_down(steps, row, col, board)


def move_right(steps, row, col, board):
    col_start = 0
    for i in range(len(board[row])):
        if board[row][i] != ' ':
            col_start = i
            break
    col_end = len(board[row]) - 1
    while steps > 0:
        if board[row][col] == '.':
            steps -= 1
            col += 1
        if col > col_end:
            col = col_start
        if board[row][col] == '#':
            col -= 1
            if col < col_start:
                col = col_end
            return row, col
    return row, col


def move_left(steps, row, col, board):
    col_start = 0
    for i in range(len(board[row])):
        if board[row][i] != ' ':
            col_start = i
            break
    col_end = len(board[row]) - 1
    while steps > 0:
        if board[row][col] == '.':
            steps -= 1
            col -= 1
        if col < col_start:
            col = col_end
        if board[row][col] == '#':
            col += 1
            if col > col_end:
                col = col_start
            return row, col
    return row, col


def move_up(steps, row, col, board):
    row_start = 0
    for i in range(len(board)):
        if len(board[i]) - 1 >= col and board[i][col] != ' ':
            row_start = i
            break
    row_end = 0
    for i in range(row_start, len(board)):
        if len(board[i]) - 1 >= col and board[i][col] != ' ':
            row_end = i
    while steps > 0:
        if board[row][col] == '.':
            steps -= 1
            row -= 1
        if row < row_start:
            row = row_end
        if board[row][col] == '#':
            row += 1
            if row > row_end:
                row = row_start
            return row, col
    return row, col


def move_down(steps, row, col, board):
    row_start = 0
    for i in range(len(board)):
        if len(board[i]) - 1 >= col and board[i][col] != ' ':
            row_start = i
            break
    row_end = 0
    for i in range(row_start, len(board)):
        if len(board[i]) - 1 >= col and board[i][col] != ' ':
            row_end = i
    while steps > 0:
        if board[row][col] == '.':
            steps -= 1
            row += 1
        if row > row_end:
            row = row_start
        if board[row][col] == '#':
            row -= 1
            if row < row_start:
                row = row_end
            return row, col
    return row, col


with open('input.txt') as f:
    start = time.time()
    parts = f.read().split('\n\n')
    board = [i for i in parts[0].split('\n')]
    directions = re.findall(r'\d+|L|R', parts[1].strip())
    directions = [int(i) if i.isnumeric() else i for i in directions]
    direction_facing = dict()
    direction_facing['R'] = {'L': 'U',
                             'R': 'D',
                             'U': 'R',
                             'D': 'L'}
    direction_facing['L'] = {'L': 'D',
                             'R': 'U',
                             'U': 'L',
                             'D': 'R'}
    row = 0
    col = 0
    for i in range(len(board[row])):
        if board[row][i] != ' ':
            col = i
            break
    facing = 'R'
    for direction in directions:
        if isinstance(direction, int):
            row, col = move(direction, facing, row, col, board)
        else:
            facing = direction_facing[direction][facing]
    row = row + 1
    col = col + 1
    face_value = {'R': 0, 'D': 1, 'L': 2, 'U': 3}
    final_password = 1000 * row + 4 * col + face_value[facing]
    print('Final password :', final_password)
    print('Time taken :', time.time() - start)
