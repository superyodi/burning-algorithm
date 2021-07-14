# 백준 - 키순서


import sys

# [Try 1. dictionary 두개로 부르트포스 ] 51776KB,	2160ms
'''
input = sys.stdin.readline
N, M = map(int, input().split(" "))

taller = {i + 1: set() for i in range(N)}
shorter = {i + 1: set() for i in range(N)}

for _ in range(M):
    a, b = map(int, input().split(" "))
    taller[a].add(b)
    shorter[b].add(a)

for n in range(1, N + 1):
    for t in taller[n]:
        shorter[t] |= shorter[n]

    for s in shorter[n]:
        taller[s] |= taller[n]

for n in range(1, N + 1):
    for t in taller[n]:
        shorter[t] |= shorter[n]

    for s in shorter[n]:
        taller[s] |= taller[n]

answer = 0

for n in range(1, N + 1):
    if len(taller[n]) + len(shorter[n]) == N - 1:
        answer += 1

print(answer)

'''

# [Try 2. 플로이드 와샬 ] 127352KB,	1696ms

# node가 다른 모든 노드와 연결이 되어있는지 찾는 문제

input = sys.stdin.readline
N, M = map(int, input().split(" "))
graph = [[False for _ in range(N+1)] for _ in range(N+1)]


for _ in range(M):
    a, b = map(int, input().split(" "))
    graph[a][b] = True


# floyed algorithm

answer = 0
for k in range(1,N+1):
    for j in range(1, N + 1):
        for i in range(1, N + 1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = True



answer = 0
for i in range(1, N+1):
    cnt = 0
    for j in range(1, N+1):
        if graph[i][j] or graph[j][i]: cnt += 1

    if cnt == N-1: answer += 1

print(answer)