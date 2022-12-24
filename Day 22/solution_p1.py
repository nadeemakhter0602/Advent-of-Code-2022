import re
import time


with open('input.txt') as f:
    start = time.time()
    parts = f.read().split('\n\n')
    board = [i for i in parts[0].split('\n')]
    directions = re.findall(r'\d+|L|R', parts[1].strip())
    directions = [int(i) if i.isnumeric() else i for i in directions]
    row = 0
    col = 0
    for i in range(len(board[row])):
        if board[row][i] != ' ':
            col = i
            break
    facing = 'R'
    for direction in directions:
        if direction == 'R':
            if facing == 'L':
                facing = 'U'
            elif facing == 'R':
                facing = 'D'
            elif facing == 'U':
                facing = 'R'
            elif facing == 'D':
                facing = 'L'
        elif direction == 'L':
            if facing == 'L':
                facing = 'D'
            elif facing == 'R':
                facing = 'U'
            elif facing == 'U':
                facing = 'L'
            elif facing == 'D':
                facing = 'R'
        elif isinstance(direction, int):
            if facing == 'R':
                col_start = 0
                for i in range(len(board[row])):
                    if board[row][i] != ' ':
                        col_start = i
                        break
                col_end = len(board[row]) - 1
                while direction > 0:
                    if board[row][col] == '.':
                        direction -= 1
                        col += 1
                    if col > col_end:
                        col = col_start
                    if board[row][col] == '#':
                        col -= 1
                        if col < col_start:
                            col = col_end
                        break
            elif facing == 'L':
                col_start = 0
                for i in range(len(board[row])):
                    if board[row][i] != ' ':
                        col_start = i
                        break
                col_end = len(board[row]) - 1
                while direction > 0:
                    if board[row][col] == '.':
                        direction -= 1
                        col -= 1
                    if col < col_start:
                        col = col_end
                    if board[row][col] == '#':
                        col += 1
                        if col > col_end:
                            col = col_start
                        break
            elif facing == 'U':
                row_start = 0
                for i in range(len(board)):
                    if len(board[i]) - 1 >= col and board[i][col] != ' ':
                        row_start = i
                        break
                row_end = 0
                for i in range(row_start, len(board)):
                    if len(board[i]) - 1 >= col and board[i][col] != ' ':
                        row_end = i
                while direction > 0:
                    if board[row][col] == '.':
                        direction -= 1
                        row -= 1
                    if row < row_start:
                        row = row_end
                    if board[row][col] == '#':
                        row += 1
                        if row > row_end:
                            row = row_start
                        break
            elif facing == 'D':
                row_start = 0
                for i in range(len(board)):
                    if len(board[i]) - 1 >= col and board[i][col] != ' ':
                        row_start = i
                        break
                row_end = 0
                for i in range(row_start, len(board)):
                    if len(board[i]) - 1 >= col and board[i][col] != ' ':
                        row_end = i
                while direction > 0:
                    if board[row][col] == '.':
                        direction -= 1
                        row += 1
                    if row > row_end:
                        row = row_start
                    if board[row][col] == '#':
                        row -= 1
                        if row < row_start:
                            row = row_end
                        break
    row = row + 1
    col = col + 1
    face_value = {'R': 0, 'D': 1, 'L': 2, 'U': 3}
    final_password = 1000 * row + 4 * col + face_value[facing]
    print('Final password :', final_password)
    print('Time taken :', time.time() - start)
