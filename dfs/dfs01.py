# BOJ_13023 ABCDE

# 인접행렬로 구현한 버전
N, M = map(int, input().split())
# count = 0
graph = [[0 for _ in range(N)] for _ in range(N)]

# 그래프 생성
for _ in range(0, M):
    i, j = map(int, input().split())
    graph[i][j] = 1
    graph[j][i] = 1

# 그래프 순회
visited = [0 for _ in range(N)]
stack = []
list = []

# 인접행렬로 dfs
def dfs(start):
    stack.append(start)
    while stack:
        current = stack.pop()
       
        if not visited[current]:
            visited[current] = 1
            list.append(current)
            # print("지금은 {}에 있으요".format(current))

            for i in range(N):
                if graph[current][i] == 1:
                    stack.append(i)


for i in range(N):
    dfs(i)

print(list)
