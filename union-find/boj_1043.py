# 백준 거짓말
# union find

import sys

# parent, child
def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def find(a):
    if parents[a] == a:
        return a
    parents[a] = find(parents[a])
    return parents[a]


N, M = map(int, sys.stdin.readline().split(' '))

parents = [i for i in range(N + 1)]

line = list(map(int, sys.stdin.readline().split(' ')))
true_num = line[0]

if true_num != 0:
    trues = line[1:]
    partys = []

    for _ in range(M):
        line = list(map(int, sys.stdin.readline().split(' ')))
        party = line[1:]
        partys.append(party)

        tmp = party[0]
        for per in party:
            union(tmp, per)

    cnt = 0
    for party in partys:
        per = parents[party[0]]
        for true in trues:
            if find(true) == find(per):
                break

        else:
            cnt += 1
    print(cnt)

else:
    for _ in range(M):
        sys.stdin.readline()
    print(M)

'''
6 5
1 6
2 1 2
2 2 3
2 3 4
2 4 5
2 5 6

'''

'''
6 5
1 6
2 4 5
2 1 2
2 2 3
2 3 4
2 5 6

'''

'''
5 3
1 3
3 1 2 4
3 1 4 5
1 3

'''
