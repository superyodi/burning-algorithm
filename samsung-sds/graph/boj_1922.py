# 백준 - 네트워크 연결

import sys, collections

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [dict() for _ in range(N+1)]
weights = []
parents = [i for i in range(N+1)]
visited = [[False for _ in range(N+1)] for _ in range(N+1)]
cost_sum = 0

def find(node):
    if node == parents[node]: return node

    parents[node] = find(parents[node])
    return parents[node]

def union(n1, n2):
    p1 = find(n1)
    p2 = find(n2)

    if p1 != p2:
        parents[p1] = p2
        return False

    return True



# init graph
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split(" "))
    weights.append([c,a,b])

weights.sort()

for w, a, b in weights:
    if not visited[a][b] and not visited[b][a] and not union(a, b):
        cost_sum += w
        union(a, b)
        visited[a][b] = True
        visited[b][a] = True

print(cost_sum)







