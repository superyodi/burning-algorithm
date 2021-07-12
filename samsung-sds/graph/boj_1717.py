# 백준 - 집합의 표현

import sys

N, M = map(int, sys.stdin.readline().split(" "))
parents = [i for i in range(N + 1)]


def find(node):
    if node == parents[node]:
        return node
    parents[node] = find(parents[node])
    return parents[node]

def merge(node1, node2):
    p_node1 = find(node1)
    p_node2 = find(node2)

    if p_node1 == p_node2: return

    parents[p_node2] = p_node1
    return


for _ in range(M):
    cmd, a, b = map(int, sys.stdin.readline().split(" "))

    if cmd == 0:
        merge(a, b)
        # 합집합
        pass

    elif cmd == 1:
        # 포함하는지 확인
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")

print(parents)