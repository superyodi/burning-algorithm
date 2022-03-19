# 백준 회사문화1

import sys

n, m = map(int, sys.stdin.readline().split(' '))
nums= list(map(int, sys.stdin.readline().split(' ')))
answer = [0 for i in range(n)]

graph = [[] for i in range(n)]


for i in range(1, n):
    graph[nums[i] - 1].append(i)

for _ in range(m):
    i, w = map(int, sys.stdin.readline().split(' '))
    answer[i-1] += w

# dfs
stack = [0]
while stack:
    node = stack.pop()

    for next in graph[node]:
        answer[next] += answer[node]
        stack.append(next)

for i in range(n):
    print(answer[i], end=' ')


'''
5 3
-1 1 2 3 4
2 2
3 4
5 6
'''

'''
11 6
-1 1 1 2 3 3 4 7 6 6 10
2 3
5 2
7 5
6 4
9 1
11 2

output: 0 3 0 3 2 4 8 8 5 4 6 

'''