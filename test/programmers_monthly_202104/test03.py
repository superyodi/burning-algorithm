import collections

def solution(a, edges):
    if set(a) == {0}:
        return 0

    if sum(a):
        return -1

    # 그래프 만들기
    graph = dict()

    for i, val in enumerate(a):
        graph[i] = set()

    for e1, e2 in edges:
        graph[e1].add(e2)
        graph[e2].add(e1)

    queue = collections.deque()

    for n in graph:
        if len(graph[n]) == 1:
            queue.append(n)

    visited = [False] * len(a)
    cnt = 0

    while queue:
        now = queue.popleft()

        if not visited[now]:

            visited[now] = True

            for node in graph[now]:
                if not visited[node]:
                    a[node] += a[now]
                    cnt += abs(a[now])
                    a[now] = 0

                    queue.append(node)

    if sum(a):
        return -1

    return cnt

'''
정확도 66% 

시간초과 이슈가 발생한것 같다.
dp를 어떻게 해야할지 잘 모르겠다

'''