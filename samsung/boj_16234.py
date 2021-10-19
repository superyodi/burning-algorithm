# 백준 - 인구 이동


import sys, collections

N, L, R = map(int, sys.stdin.readline().split(' '))

arr = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    line = list(map(int, sys.stdin.readline().split(' ')))
    for j in range(N):
        arr[i][j] = line[j]

cnt = 0

def calc():
    global cnt

    while True:
        visited = [[False for _ in range(N)] for _ in range(N)]
        flag = False

        for r in range(N):
            for c in range(N):
                if not visited[r][c]:
                    if bfs(visited, r, c):
                        flag = True

        if flag == False: break

        if flag: cnt += 1



def bfs(visited, r, c):
    q = collections.deque()
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    q.append([r, c])
    sub_cnt = 0
    sub_sum = 0
    sub = []

    while q:
        r, c = q.popleft()
        if visited[r][c]: continue
        visited[r][c] = True
        sub_cnt += 1
        sub_sum += arr[r][c]
        sub.append([r, c])

        for dir in dirs:
            nr, nc = r + dir[0], c + dir[1]

            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc] and L <= abs(arr[r][c] - arr[nr][nc]) <= R:
                    q.append([nr, nc])


    if len(sub) < 2: return False
    val = sub_sum // sub_cnt

    for r, c in sub:
        arr[r][c] = val

    return True


calc()
print(cnt)
