# DFS와 BFS
# https://www.acmicpc.net/problem/1260
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
result = []

def bfs(v):
    queue = []
    queue.append(v)

    while queue:
        now = queue.pop(0)
        # print("queue: ", queue)
        if not visited[now]:
            visited[now] = True
            result.append(now)

            child_sort = sorted(graph[now])
            for c in child_sort:
                queue.append(c)


def dfs(v):
    stack = []
    stack.append(v)

    while stack:
        now = stack.pop()
        # print("stack: ", stack)
        if not visited[now]:
            visited[now] = True
            result.append(now)

            child_sort = sorted(graph[now], reverse=True)
            for c in child_sort:
                stack.append(c)


# graph 입력
for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)


dfs(V)
print("리스트 출력: ")
print(result)
print("요구되는 출력값: ")
print(" ".join(map(str, result)))

visited = [False for _ in range(N+1)]
result.clear()

bfs(V)
print("리스트 출력: ")
print(result)
print("요구되는 출력값: ")
print(" ".join(map(str, result)))
