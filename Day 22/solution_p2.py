import re
import time


def move(steps, facing, row, col, board, wrap_around):
    if facing == 'R':
        return move_right(steps, row, col, board, wrap_around, facing)
    elif facing == 'L':
        return move_left(steps, row, col, board, wrap_around, facing)
    elif facing == 'U':
        return move_up(steps, row, col, board, wrap_around, facing)
    elif facing == 'D':
        return move_down(steps, row, col, board, wrap_around, facing)


def reverse_facing(facing):
    if facing == 'L':
        return 'R'
    elif facing == 'U':
        return 'D'
    elif facing == 'D':
        return 'U'
    elif facing == 'R':
        return 'L'


def move_right(steps, row, col, board, wrap_around, facing):
    col_start = 0
    for i in range(len(board[row])):
        if board[row][i] != ' ':
            col_start = i
            break
    col_end = len(board[row]) - 1
    if board[row][col] == '#':
        row, col, facing = wrap_around[(row, col, 'L')]
        return row, col, reverse_facing(facing)
    while steps > 0:
        if board[row][col] == '.':
            steps -= 1
            col += 1
        if col > col_end:
            row, col, facing = wrap_around[(row, col_end, facing)]
            return move(steps, facing, row, col, board, wrap_around)
        if board[row][col] == '#':
            col -= 1
            return row, col, facing
    return row, col, facing


def move_left(steps, row, col, board, wrap_around, facing):
    col_start = 0
    for i in range(len(board[row])):
        if board[row][i] != ' ':
            col_start = i
            break
    col_end = len(board[row]) - 1
    if board[row][col] == '#':
        row, col, facing = wrap_around[(row, col, 'R')]
        return row, col, reverse_facing(facing)
    while steps > 0:
        if board[row][col] == '.':
            steps -= 1
            col -= 1
        if col < col_start:
            row, col, facing = wrap_around[(row, col_start, facing)]
            return move(steps, facing, row, col, board, wrap_around)
        if board[row][col] == '#':
            col += 1
            return row, col, facing
    return row, col, facing


def move_up(steps, row, col, board, wrap_around, facing):
    row_start = 0
    for i in range(len(board)):
        if len(board[i]) - 1 >= col and board[i][col] != ' ':
            row_start = i
            break
    row_end = 0
    for i in range(row_start, len(board)):
        if len(board[i]) - 1 >= col and board[i][col] != ' ':
            row_end = i
    if board[row][col] == '#':
        row, col, facing = wrap_around[(row, col, 'D')]
        return row, col, reverse_facing(facing)
    while steps > 0:
        if board[row][col] == '.':
            steps -= 1
            row -= 1
        if row < row_start:
            row, col, facing = wrap_around[(row_start, col, facing)]
            return move(steps, facing, row, col, board, wrap_around)
        if board[row][col] == '#':
            row += 1
            return row, col, facing
    return row, col, facing


def move_down(steps, row, col, board, wrap_around, facing):
    row_start = 0
    for i in range(len(board)):
        if len(board[i]) - 1 >= col and board[i][col] != ' ':
            row_start = i
            break
    row_end = 0
    for i in range(row_start, len(board)):
        if len(board[i]) - 1 >= col and board[i][col] != ' ':
            row_end = i
    if board[row][col] == '#':
        row, col, facing = wrap_around[(row, col, 'U')]
        return row, col, reverse_facing(facing)
    while steps > 0:
        if board[row][col] == '.':
            steps -= 1
            row += 1
        if row > row_end:
            row, col, facing = wrap_around[(row_end, col, facing)]
            return move(steps, facing, row, col, board, wrap_around)
        if board[row][col] == '#':
            row -= 1
            return row, col, facing
    return row, col, facing


def fold_into_cube(cube_side, row, col, wrap_around):
    # first face of cube
    row_start_1 = row
    row_end_1 = cube_side - 1
    col_start_1 = col
    col_end_1 = col + cube_side - 1
    # second face of cube
    row_start_2 = row_start_1
    row_end_2 = row_end_1
    col_start_2 = col_end_1 + 1
    col_end_2 = col_start_2 + cube_side - 1
    # third face of cube
    row_start_3 = row_end_1 + 1
    row_end_3 = row_start_3 + cube_side - 1
    col_start_3 = col_start_1
    col_end_3 = col_end_1
    # fourth face of cube
    row_start_4 = row_end_3 + 1
    row_end_4 = row_start_4 + cube_side - 1
    col_start_4 = row
    col_end_4 = col_start_4 + cube_side - 1
    # fifth face of cube
    row_start_5 = row_start_4
    row_end_5 = row_end_4
    col_start_5 = col_end_4 + 1
    col_end_5 = col_start_5 + cube_side - 1
    # sixth face of cube
    row_start_6 = row_end_5 + 1
    row_end_6 = row_start_6 + cube_side - 1
    col_start_6 = row
    col_end_6 = col_start_6 + cube_side - 1
    # edges of first face
    top_1 = [(row_start_1, i) for i in range(col_start_1, col_end_1 + 1)]
    left_1 = [(i, col_start_1) for i in range(row_start_1, row_end_1 + 1)]
    right_1 = [(i, col_end_1) for i in range(row_start_1, row_end_1 + 1)]
    bottom_1 = [(row_end_1, i) for i in range(col_start_1, col_end_1 + 1)]
    # edges for second face
    top_2 = [(row_start_2, i) for i in range(col_start_2, col_end_2 + 1)]
    left_2 = [(i, col_start_2) for i in range(row_start_2, row_end_2 + 1)]
    right_2 = [(i, col_end_2) for i in range(row_start_2, row_end_2 + 1)]
    bottom_2 = [(row_end_2, i) for i in range(col_start_2, col_end_2 + 1)]
    # edges for third face
    top_3 = [(row_start_3, i) for i in range(col_start_3, col_end_3 + 1)]
    left_3 = [(i, col_start_3) for i in range(row_start_3, row_end_3 + 1)]
    right_3 = [(i, col_end_3) for i in range(row_start_3, row_end_3 + 1)]
    bottom_3 = [(row_end_3, i) for i in range(col_start_3, col_end_3 + 1)]
    # edges for fourth face
    top_4 = [(row_start_4, i) for i in range(col_start_4, col_end_4 + 1)]
    left_4 = [(i, col_start_4) for i in range(row_start_4, row_end_4 + 1)]
    right_4 = [(i, col_end_4) for i in range(row_start_4, row_end_4 + 1)]
    bottom_4 = [(row_end_4, i) for i in range(col_start_4, col_end_4 + 1)]
    # edges for fifth face
    top_5 = [(row_start_5, i) for i in range(col_start_5, col_end_5 + 1)]
    left_5 = [(i, col_start_5) for i in range(row_start_5, row_end_5 + 1)]
    right_5 = [(i, col_end_5) for i in range(row_start_5, row_end_5 + 1)]
    bottom_5 = [(row_end_5, i) for i in range(col_start_5, col_end_5 + 1)]
    # edges for sixth face
    top_6 = [(row_start_6, i) for i in range(col_start_6, col_end_6 + 1)]
    left_6 = [(i, col_start_6) for i in range(row_start_6, row_end_6 + 1)]
    right_6 = [(i, col_end_6) for i in range(row_start_6, row_end_6 + 1)]
    bottom_6 = [(row_end_6, i) for i in range(col_start_6, col_end_6 + 1)]
    # connect edges
    for i in range(cube_side):
        # top of 1 and left of 6
        wrap_around[(*top_1[i], 'U')] = (*left_6[i], 'R')
        wrap_around[(*left_6[i], 'L')] = (*top_1[i], 'D')
        # left of 1 and left of 4, mirrored
        wrap_around[(*left_1[i], 'L')] = (*left_4[-(i + 1)], 'R')
        wrap_around[(*left_4[-(i + 1)], 'L')] = (*left_1[i], 'R')
        # right of 1 and left of 2
        wrap_around[(*right_1[i], 'R')] = (*left_2[i], 'R')
        wrap_around[(*left_2[i], 'L')] = (*right_1[i], 'L')
        # bottom of 1 and top of 3
        wrap_around[(*bottom_1[i], 'D')] = (*top_3[i], 'D')
        wrap_around[(*top_3[i], 'U')] = (*bottom_1[i], 'U')
        # top of 2 and bottom of 6
        wrap_around[(*top_2[i], 'U')] = (*bottom_6[i], 'U')
        wrap_around[(*bottom_6[i], 'D')] = (*top_2[i], 'D')
        # right of 2 and right of 5, mirrored
        wrap_around[(*right_2[-(i+1)], 'R')] = (*right_5[i], 'L')
        wrap_around[(*right_5[i], 'R')] = (*right_2[-(i+1)], 'L')
        # bottom of 2 and right of 3
        wrap_around[(*bottom_2[i], 'D')] = (*right_3[i], 'L')
        wrap_around[(*right_3[i], 'R')] = (*bottom_2[i], 'U')
        # left of 3 and top of 4
        wrap_around[(*left_3[i], 'L')] = (*top_4[i], 'D')
        wrap_around[(*top_4[i], 'U')] = (*left_3[i], 'R')
        # bottom of 3 and top of 5
        wrap_around[(*bottom_3[i], 'D')] = (*top_5[i], 'D')
        wrap_around[(*top_5[i], 'U')] = (*bottom_3[i], 'U')
        # right of 4 and left of 5
        wrap_around[(*right_4[i], 'R')] = (*left_5[i], 'R')
        wrap_around[(*left_5[i], 'L')] = (*right_4[i], 'L')
        # bottom of 4 and top of 6
        wrap_around[(*bottom_4[i], 'D')] = (*top_6[i], 'D')
        wrap_around[(*top_6[i], 'U')] = (*bottom_4[i], 'U')
        # right of 6 and bottom of 5
        wrap_around[(*right_6[i], 'R')] = (*bottom_5[i], 'U')
        wrap_around[(*bottom_5[i], 'D')] = (*right_6[i], 'L')
    return wrap_around


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
    cube_side = 50
    wrap_around = fold_into_cube(cube_side, row, col, dict())
    for direction in directions:
        if isinstance(direction, int):
            row, col, facing = move(
                direction, facing, row, col, board, wrap_around)
        else:
            facing = direction_facing[direction][facing]
    row = row + 1
    col = col + 1
    face_value = {'R': 0, 'D': 1, 'L': 2, 'U': 3}
    final_password = 1000 * row + 4 * col + face_value[facing]
    print('Final password :', final_password)
    print('Time taken :', time.time() - start)
