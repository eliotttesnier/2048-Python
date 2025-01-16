## 2048 logic

import random
import time

def can_move(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return True
            if i > 0 and board[i][j] == board[i - 1][j]:
                return True
            if i < len(board) - 1 and board[i][j] == board[i + 1][j]:
                return True
            if j > 0 and board[i][j] == board[i][j - 1]:
                return True
            if j < len(board[i]) - 1 and board[i][j] == board[i][j + 1]:
                return True
    return False

def generate(board):
    random.seed(time.time())
    empty_cells = [(i, j) for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == 0]
    if not empty_cells:
        return board

    i, j = random.choice(empty_cells)
    board[i][j] = 2 if random.random() < 0.9 else 4
    return board

def right(board):
    for line in board:
        new_line = [num for num in line if num != 0]

        for i in range(len(new_line) - 1, 0, -1):
            if new_line[i] == new_line[i - 1]:
                new_line[i] *= 2
                new_line[i - 1] = 0

        new_line = [num for num in new_line if num != 0]
        new_line = [0] * (len(line) - len(new_line)) + new_line

        for i in range(len(line)):
            line[i] = new_line[i]
    return board

def left(board):
    for line in board:
        new_line = [num for num in line if num != 0]

        for i in range(len(new_line) - 1):
            if new_line[i] == new_line[i + 1]:
                new_line[i] *= 2
                new_line[i + 1] = 0

        new_line = [num for num in new_line if num != 0]
        new_line += [0] * (len(line) - len(new_line))

        for i in range(len(line)):
            line[i] = new_line[i]
    return board

def up(board):
    board = [list(row) for row in zip(*board)]
    board = left(board)
    board = [list(row) for row in zip(*board)]
    return board

def down(board):
    board = [list(row) for row in zip(*board)]
    board = right(board)
    board = [list(row) for row in zip(*board)]
    return board