# 백준 -드래곤 커브

import sys

N = int(sys.stdin.readline())

arr = [[False for _ in range(101)] for _ in range(101)]

def dfs(sx,sy,sd,g):
    dirs = ((0, 1), (-1, 0), (0, -1), (1, 0))
    draw = []
    cache = []

    cur_gen = 0
    pre_x, pre_y = 0, 0

    while True:
        if cur_gen == 0:
            arr[sy][sx] = True
            sy2, sx2 = sy + dirs[sd][0], sx + dirs[sd][1]
            arr[sy2][sx2] = True
            pre_y, pre_x = sy2, sx2
            draw.append(sd)
            cache.append(sd)

        if cur_gen == g: break
        # 회전 기준점 pop
        while draw:
            d = draw.pop()
            nd = (d + 1) % 4
            ny, nx = pre_y + dirs[nd][0], pre_x + dirs[nd][1]
            arr[ny][nx] = True
            pre_y, pre_x = ny, nx
            cache.append(nd)

        draw = cache.copy()
        cur_gen += 1

def find(r,c):
    if r- 1 < 0 or c -1 < 0:
        return False
    if arr[r-1][c-1] and arr[r-1][c] and arr[r][c-1]:
        return True

for _ in range(N):
    x, y, d, g = map(int, sys.stdin.readline().split(' '))
    dfs(x,y,d,g) # do dragon curve

ans = 0
for i in range(101):
    for j in range(101):
        if arr[i][j]:
            if find(i,j): ans += 1

        # find square
print(ans)
