import sys


def build_runway(road, N, K):
    # 경사로 head
    h = 0
    visited = [False] * N
    for i in range(1, len(road)):
        if abs(road[h] - road[i]) > 1: return False
        if road[h] == road[i]:
            h = i
            continue

        # 쪽 || 아래 방향 경사로 건설
        if road[h] < road[i]:
            for j in range(K):
                if h-j < 0 or visited[h-j] or road[h-j] != road[h]:
                    return False
                visited[h - j] = True
            h = i

        # 오른쪽 || 위 방향 경사로 건설
        else:
            for j in range(K):
                if i+j >= N or visited[i+j] or road[i+j] != road[i]:
                    return False
                visited[i+j] = True

            h = i+K-1
            i += K

    return True



N, K = map(int, sys.stdin.readline().split(' '))
road = []
for _ in range(N):
    line = list(map(int, sys.stdin.readline().split(' ')))
    road.append(line)

count = 0

# 가로 검사
# print("row")
for r in range(N):
    line = []
    for c in range(N):
        line.append(road[r][c])

    if build_runway(line, N, K):
        count += 1
        # print(line)

# print("colm")
# 세로 검사
for c in range(N):
    line = []
    for r in range(N):
        line.append(road[r][c])

    if build_runway(line, N, K):
        count += 1
        # print(line)


print(count)
