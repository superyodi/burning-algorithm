import collections


def solution(n, edge):
    graph = {i + 1: set() for i in range(n)}
    depth_dict = dict()

    # make graph
    for n1, n2 in edge:
        graph[n1].add(n2)
        graph[n2].add(n1)

    visited = [False for i in range(n + 1)]

    queue = collections.deque()
    queue.append((1, 0))
    max_depth = 0

    while queue:
        node, depth = queue.popleft()

        if visited[node]:
            continue
        visited[node] = True

        max_depth = max(depth, max_depth)

        if depth not in depth_dict:
            depth_dict[depth] = 0
        depth_dict[depth] += 1

        for child in graph[node]:
            if not visited[child]:
                queue.append((child, depth + 1))

    if max_depth == 0:
        return 0

    return depth_dict[max_depth]

