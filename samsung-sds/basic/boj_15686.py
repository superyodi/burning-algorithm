# 백준 - 치킨 배달

import sys

N, M = map(int, sys.stdin.readline().split(" "))
selected_chickens = []
chickens = []
houses = []
min_sum = -1
visited = [[False for _ in range(N)] for _ in range(N)]

# head는 중복을 막기위함 (치킨집의 조합을 구해야하므로 )
def dfs(head, cnt):
    global min_sum, visited
    print(selected_chickens, cnt)
    if cnt == M:
        chicken_sum = 0

        for hy, hx in houses:
            chicken_road = -1
            for cy, cx in selected_chickens:
                if visited[cy][cx]:
                    now_road = abs(cy - hy) + abs(cx - hx)
                    if chicken_road == -1: chicken_road = now_road
                    chicken_road = min(chicken_road, now_road)

            chicken_sum += chicken_road

        if min_sum== -1: min_sum = chicken_sum
        min_sum = min(min_sum, chicken_sum)
        return

    for i in range(head, len(chickens)):
        cy, cx = chickens[i]

        if not visited[cy][cx]:
            visited[cy][cx] = True
            selected_chickens.append((cy, cx))
            dfs(i, cnt+1) # 여기 진짜 중요!!
            visited[cy][cx] = False
            selected_chickens.pop()


for r in range(N):
    line = list(map(int, sys.stdin.readline().split(" ")))
    for c in range(N):
        if line[c] == 2:
            chickens.append((r,c))
        elif line[c] == 1:
            houses.append((r,c))


dfs(0,0)
print(min_sum)
