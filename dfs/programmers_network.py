# 프로그래머스 네트워크
# https://programmers.co.kr/learn/courses/30/lessons/43162

route_list = set()

def solution(n, computers):

    for i in range(n):
        computers[i][i] = 0

    for node in range(n):
        print(node,'번째 노드')
        route_list.add(dfs(node, computers, stack=[]))

    answer = len(route_list)
    print(answer)
    return answer

def dfs(start, computers, stack):
    visited = [False] * len(computers)
    visited_node = []
    stack.append(start)

    while stack:
        now = stack.pop()

        # 이전에 방문경험없다면
        if not visited[now]:
            visited[now] = True
            visited_node.append(now)

            # 자식노드가 있다면
            for child in range(len(computers[now])):
                if computers[now][child]:
                    print("child: ",child)
                    stack.append(child)

    str_visited = ''.join(map(str, sorted(visited_node)))
    return str_visited

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])