# 백준 - 게임 개발

import sys
import collections

input = sys.stdin.readline

N = int(input())
indegrees = [0] * (N+1)
times = [0] * (N+1)
dp = [0] * (N+1)
graph = {i+1 : set() for i in range(N)}



for n in range(N):
    now = n+1
    line = list(map(int, input().split(" ")))
    times[now] = line[0]

    for i in range(1,len(line)):
        node = line[i]
        if node == -1: break

        graph[node].add(now)
        indegrees[now] += 1

queue = collections.deque()

for i in range(1, N+1):
    if indegrees[i] == 0:
        queue.append(i)
        dp[i] = times[i]



while queue:

    now = queue.popleft()

    for next in graph[now]:
        indegrees[next] -= 1
        dp[next] = max(dp[next], dp[now] + times[next])

        if indegrees[next] == 0:
            queue.append(next)


for i in range(1, N+1):
    print(dp[i])


'''
5
10 -1
10 1 -1
4 1 2 -1
4 3 1 -1
3 3 4 -1

'''

'''
3
10 -1
20 -1
3 1 2 -1

'''

'''
4
1 4 3 2 -1
2 4 -1
1 4 -1
1 -1

'''

'''
4
1 -1
1 1 -1
1 1 -1
1 2 3 -1

'''