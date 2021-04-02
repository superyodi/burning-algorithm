# 백준 2606 바이러
# https://www.acmicpc.net/problem/2606

# 연결되어있으면 바이러스
# 그래프 입력
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split(' '))
    graph[i].append(j)
    graph[j].append(i)

visited = [False] * (n+1)
count = -1
stack = [1,]

# 그래프 순회 (dfs)
while stack:
    node = stack.pop()
    # print(f"현재 노드는: {node}")
    if not visited[node]:
        count += 1
        visited[node] = True

    # 현재 노드의 자식노드 순회
    for child in graph[node]:
        # 자식노드 방문경험 없을때
        if not visited[child]:
            stack.append(child)


print(count)