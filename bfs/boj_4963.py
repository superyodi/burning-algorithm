# 백준 - 섬의 개수


# bfs, 완전탐색

import sys, collections


def bfs(start):
    q = collections.deque()
    q.append([start[0],start[1]])

    while q:
        r, c = q.popleft()

        if visited[r][c]: continue
        visited[r][c] = True

        # 가로 세로 대각선
        for nr in range(r-1, r+2):
            for nc in range(c-1, c+2):
                if 0<= nr < h and 0<= nc < w:
                    if not visited[nr][nc] and arr[nr][nc] == '1':
                        q.append([nr,nc])

while True:
    w, h = map(int, sys.stdin.readline().split(' '))
    if w == 0 and h == 0: break

    arr = []
    for _  in range(h):
        line = list(sys.stdin.readline().strip().split(' '))
        arr.append(line)

    visited = [[False for _ in range(w) ] for _ in range(h)]

    count = 0

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and arr[i][j] == '1':
                # print(i, j)
                bfs([i,j])

                # print(*visited, sep='\n')

                count += 1

    print(count)
