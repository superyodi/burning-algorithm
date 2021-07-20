# 백준 - 여행 가자

import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

parents = [ i for i in range(N)]

def find(a):
    if parents[a] == a: return a

    parents[a] = find(parents[a])
    return parents[a]

def union(a,b):
    a = find(a)
    b = find(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b

for i in range(N):
    line = list(map(int, sys.stdin.readline().split(" ")))
    for j in range(N):
        if line[j]:
            union(i, j)

# print(parents)

plan = list(map(lambda x : int(x)-1, sys.stdin.readline().split(" ")))
parent = -1



for i in set(plan):
    if parent != parents[i]:
        if parent == -1:
            parent = parents[i]

        else:
            print("NO")
            break
else:
    print("YES")