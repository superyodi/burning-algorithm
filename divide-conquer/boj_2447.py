# 백준 별찍기 10

import sys

# divide
def divide(n):
    global arr

    if n == 3:
        arr[0][:3] = arr[2][:3] = [1,1,1]
        arr[1][:3] = [1,0,1]
        return

    m = n // 3
    divide(m)

    # 3*3으로 나눈다
    for r in range(3):
        for c in range(3):
            if r == 1 and c == 1:
                # 빈칸으로 남겨두는 부분
                continue
            for k in range(m):
                arr[m*r+k][m*c:m*(c+1)] = arr[k][:m]



N = int(sys.stdin.readline())
# conquer
arr = [[0 for _ in range(N)] for _ in range(N)]
divide(N)

for line in arr:
    for i in line:
        if i: print('*', end = '')
        else: print(' ', end='')
    print()

