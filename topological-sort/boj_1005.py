# ACM Craft

import sys, collections

class Node:
    def __init__(self, val):
        self.val = val
        self.child = {}


def topological_sort(graph, indegree, times, goal):

    if indegree[goal] == 0:
        return times[goal]
    build_time = [0] * len(times)

    queue = collections.deque()

    # 1. start node 찾기
    for node, val in enumerate(indegree):
        if val == 0:
            queue.append(node)
            build_time[node] = times[node]

    # 2. graph의 간선 제거하면서 정렬
    visited = set()

    while queue:
        now = queue.popleft()

        if now in visited:
            continue

        visited.add(now)

        if now in graph:
            for node in graph[now]:
                indegree[node] -= 1

                # build_time update
                build_time[node] = max(build_time[node], build_time[now] + times[node])

                # 더이상 node를 가리키는 다른 노드가 없을때
                if indegree[node] == 0 and node not in visited:
                    queue.append(node)

    return build_time[goal]



T = int(sys.stdin.readline())

tc = 0
while tc < T:
    N, K = map(int, sys.stdin.readline()[:-1].split(' '))
    times = [0,]
    D = list(map(int, sys.stdin.readline().split(' ')))
    times.extend(D)

    # 인접리스트
    graph = dict()
    indegree = [0] * (N+1)

    for k in range(K):
        node, child = map(int, sys.stdin.readline().split(' '))
        if node not in graph:
            graph[node] = set()

        graph[node].add(child)
        indegree[child] += 1

    W = int(sys.stdin.readline())

    # 위상 정렬
    print(graph)
    print(topological_sort(graph, indegree, times, W))

    tc += 1

