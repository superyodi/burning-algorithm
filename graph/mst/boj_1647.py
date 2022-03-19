# 백준 - 도시 분할 계획
# MST - Kruskal
import sys, heapq

N, M = map(int, sys.stdin.readline().split(' '))
graph = [] # 가중치 인접리스트, 양방향
parents = [i for i in range(N+1)]


for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split(' '))
    heapq.heappush(graph, [c, [a,b,c]]) # 우선순위 큐, 가중치를 기준으로


def find(u):
    if parents[u] == u: return u

    parents[u] = find(parents[u])
    return parents[u]


def Kruskal():
    edgeCnt = 0
    answer = 0

    while edgeCnt != N-2:
        a,b,c = heapq.heappop(graph)[1]
        a = find(a) # find
        b = find(b)
        if a != b:
            answer += c
            parents[b] = a # union
            edgeCnt += 1

    return answer

print(Kruskal())


