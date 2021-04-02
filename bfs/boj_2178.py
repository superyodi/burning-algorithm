# 백준 2178 미로탐색
# https://www.acmicpc.net/problem/2178

# N, M 입력

N, M = map(int, input().split(' '))

# graph 입력
graph = [[0] * M for _ in range(N)]

for i in range(N):
    tmp = input()
    for j in range(M):
        graph[i][j] = int(tmp[j])

# bfs를 위한 변수 설정

# direction var
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

# visited arr
visited = [[0] * M for _ in range(N)]

# queue
queue = [(0,0)]
goal = (N-1, M-1)
visited[0][0] = 1
answer = 0

# bfs
while queue:
    y, x = queue.pop(0)

    # x, y 조건 검사
    if y == goal[0] and x == goal[1]:
        answer = visited[y][x]
        break

    for i in range(4):
        # 현재 좌표
        ny = y + dy[i]
        nx = x + dx[i]

        # 현재 x,y 좌표가 graph의 범위를 벗어나지않고
        # 이전에 방문했던 적이 없으며 그래프에 길이 있는 경우
        if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0 and graph[ny][nx] == 1:
            visited[ny][nx] = visited[y][x] + 1
            queue.append((ny, nx))

print(answer)