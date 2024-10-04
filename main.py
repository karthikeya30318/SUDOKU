import numpy as np

board = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])


def is_valid(board, row, col, num):

    if num in board[row, :]:
        return False

    if num in board[:, col]:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    if num in board[row_start:row_start + 3, col_start:col_start + 3]:
        return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row, col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row, col] = num

                        if solve_sudoku(board):
                            return True
                        board[row, col] = 0

                return False

    return True


def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))


if solve_sudoku(board):
    print("Sudoku solved successfully:")
    print_board(board)
else:
    print("No solution exists for this Sudoku puzzle.")
