# 백준 - Z

import sys
N, R, C = map(int, sys.stdin.readline().split(' '))
cnt = -1

flag = False

def divide(r, c, n):
    global cnt
    if flag: return

    # print("divide:", r, c, n)
    if n == 1:
        return conquer(r, c)

    size = 1 << n

    if r <= R < r+size and c<= C < c+size:
        size = 1 << (n-1)
        divide(r, c, n - 1) # 1사분면
        divide(r, c+size, n - 1)  # 2사분면
        divide(r+size, c, n - 1)  # 3사분면
        divide(r+size, c+size, n - 1)  # 4사분면

    else:
        cnt += size * size

def conquer(r,c):
    global flag, cnt
    if flag: return
    dirs = ((0,0), (0,1), (1,0),(1,1))

    for dir in dirs:
        nr, nc = r + dir[0], c + dir[1]
        cnt += 1

        if nr == R and nc == C:
            flag = True
            return
    return

divide(0,0,N)
print(cnt)


