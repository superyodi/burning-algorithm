# 백준 - 스도쿠

import sys


board = []
blanks = []
is_done = False

def search_nums(blank):
    global board
    y, x = blank
    nums = set(list(range(1,10)))

    for i in range(9):  # 1. 가로, 세로
        if board[y][i] in nums:
            nums.remove(board[y][i])
        if board[i][x] in nums:
            nums.remove(board[i][x])

    ny, nx  = 3 * (y//3), 3 * (x//3) # 3. 3*3 사각형
    for i in range(3):
        for j in range(3):
            if board[ny+i][nx+j] in nums:
                nums.remove(board[ny+i][nx+j])

    return nums


def dfs(idx):
    global board, is_done
    if is_done: return

    if idx == len(blanks):
        print_board()
        is_done = True
        return

    y, x = blanks[idx]

    nums = search_nums(blanks[idx])

    for num in nums:
        board[y][x] = num
        dfs(idx+1)
        board[y][x] = 0


def print_board():
    for line in board:
        print(*line)

# input
for i in range(9):
    line = list(map(int, sys.stdin.readline().split(" ")))
    board.append(line)
    for j in range(9):
        if board[i][j] == 0:
            blanks.append((i, j))


dfs(0)
