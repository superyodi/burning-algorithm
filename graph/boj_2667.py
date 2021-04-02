# 백준 2667 단지번호붙이기
# https://www.acmicpc.net/problem/2667
from pprint import pprint

n = int(input())
graph = [[0] * n for _ in range(n)]
can_visit = 0

# 그래프 입력
for i in range(n):
    tmp = input()
    for j in range(n):
        graph[i][j] = tmp[j]
        if tmp[j] == '1':
            can_visit += 1

# 단지 정하기
# 1) 단지: 연결된 집들의 모임
# 2) 연결된 집: 상,하,좌,우
# 3) 순회: DFS
dy = [1, -1, 0, 0]
dx = [0, 0 , 1, -1]

visited = [[False] * n for _ in range(n)]
cnt_visited = 0


# 전체를 다 순회할때까지
def dfs(start, num):
    stack = [start]
    cnt = 0

    while stack:
        y, x = stack.pop()

        if not visited[y][x]:
            visited[y][x] = True
            cnt += 1
            # print(f"({y}, {x})")

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0 <= ny< n and 0 <= nx < n:
                    if not visited[ny][nx] and graph[ny][nx] != '0':
                        graph[ny][nx] = num
                        stack.append((ny, nx))
    return cnt


num = 0
danji = []
for i in range(n):
    for j in range(n):
        # if cnt_visited == can_visit:
        #     break
        if not visited[i][j] and graph[i][j] == '1':
            num += 1
            cnt = dfs((i, j), num)
            danji.append(cnt)
            cnt_visited += cnt

# 그래프 출력
# 각 단지에 속하는 집의 수를 오름차순 정렬해서 출력
danji.sort()
print(len(danji))
for d in danji:
    print(d)
