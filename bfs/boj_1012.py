# 백준 - 유기농 배추

import sys, collections

T = int(sys.stdin.readline())
tc = 0

def bfs(start, M, N):
    global visited
    dirs = ((-1,0), (1,0), (0,-1), (0,1)) # 상, 하, 좌, 우
    queue = collections.deque()
    queue.append(start)

    while queue:
        i, j = queue.popleft()

        if visited[i][j]:
            continue
        visited[i][j] = True

        for dir in dirs:
            n_i, n_j = i+dir[0], j+dir[1]

            if 0<= n_i < M and 0<=n_j <N:
                if arr[n_i][n_j] and not visited[n_i][n_j]:
                    queue.append([n_i, n_j])


while tc < T:
    M, N, K = map(int ,sys.stdin.readline().split(" "))
    arr = [[False for _ in range(N)] for _ in range(M)]
    visited = [[False for _ in range(N)] for _ in range(M)]
    answer = 0

    for _ in range(K):
        i, j = map(int ,sys.stdin.readline().split(" "))
        arr[i][j] = True

    for i in range(M):
        for j in range(N):
            if arr[i][j] and not visited[i][j]:
                answer += 1
                bfs([i,j], M, N)


    print(answer)

    tc += 1