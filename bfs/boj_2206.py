# 백준 벽 부수고 이동하기


import sys, collections

N, M = map(int, sys.stdin.readline().split(' '))
arr = []
# [벽을 깬 경로, 아직 벽을 안깬 경로]
visited = [[[False, False] for _ in range(M)] for _ in range(N)]

for _ in range(N):
    arr.append(sys.stdin.readline().strip())

dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

queue = collections.deque()
queue.append([0, 0, 1, 0])
res = N * M
is_ok = False

while queue:
    r, c, dst, isBreak = queue.popleft()
    # print(r, c, dst, isBreak)
    if r == N - 1 and c == M - 1:
        res = dst
        is_ok = True
        break

    if visited[r][c][isBreak]: continue
    visited[r][c][isBreak] = True

    for dir in dirs:
        nr, nc = r + dir[0], c + dir[1]

        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == '0' and not visited[nr][nc][isBreak]:
                queue.append([nr, nc, dst + 1, isBreak])
            else:
                if not isBreak:
                    queue.append([nr, nc, dst + 1, 1])

if not is_ok:
    print(-1)
else:
    print(res)

'''
6 6
000001
001000
010001
100001
010110
010000
'''

'''
5 10
0000011000
1101011010
0000000010
1111111110
1111000000

14

'''