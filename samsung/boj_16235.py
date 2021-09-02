# 백준 - 나무 재테크

import sys, heapq

N, M, K = map(int, sys.stdin.readline().split(' '))

A = [[0 for _ in range(N + 1)] for _ in range(N + 1)]  # 양분
land = [[5 for _ in range(N + 1)] for _ in range(N + 1)]  # 땅
trees = [[[] for _ in range(N + 1)] for _ in range(N + 1)]  # 나무

for i in range(N):
    line = list(map(int, sys.stdin.readline().split(' ')))
    for j in range(N):
        A[i + 1][j + 1] = line[j]

for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split(' '))
    trees[x][y].append(z)


def spring_and_summer():
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if trees[r][c]:

                trees[r][c].sort()
                dead = []
                alive = []
                for tree in trees[r][c]:

                    if land[r][c] < tree:
                        dead.append(tree)
                    else:
                        land[r][c] -= tree
                        alive.append(tree+1)

                trees[r][c] = alive[:]
                for _tree in dead:
                    land[r][c] += _tree // 2


def fall():
    dirs = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            for tree in trees[r][c]:
                if tree % 5 == 0:
                    for i, j in dirs:
                        if 0 < r + i <= N and 0 < c + j <= N:
                            trees[r + i][c + j].append(1)


def winter():
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            land[r][c] += A[r][c]


def count_tree():
    cnt = 0
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            cnt += len(trees[r][c])
    return cnt


for _ in range(K):
    spring_and_summer()
    fall()
    winter()

print(count_tree())

