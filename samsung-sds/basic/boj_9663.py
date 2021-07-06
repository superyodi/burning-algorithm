# 백준 - N-Queen

import sys

N = int(sys.stdin.readline())
answer = 0
visited = [[-1 for _ in range(N)] for _ in range(N)]


def recursive(line):
    global answer, visited
    if line == N:
        answer += 1
        return

    # queen의 위치는 [line][q]
    for q in range(N):
        if visited[line][q] != -1: continue
        visited[line][q] = line

        for y in range(line, N):  # 하
            if visited[y][q] == -1:
                visited[y][q] = line

        for i in range(1, N - line):  # 대각선
            y, left_x, right_x = line + i, q + i, q - i

            if 0 <= left_x < N:
                if visited[y][left_x] == -1:
                    visited[y][left_x] = line
            if 0 <= right_x < N:
                if visited[y][right_x] == -1:
                    visited[y][right_x] = line

        recursive(line + 1)

        visited[line][q] = -1

        # 하
        for y in range(line + 1, N):
            if visited[y][q] == line:
                visited[y][q] = -1

        # 대각선
        for i in range(1, N - line):
            y, left_x, right_x = line + i, q + i, q - i

            if 0 <= left_x < N:
                if visited[y][left_x] == line:
                    visited[y][left_x] = -1
            if 0 <= right_x < N:
                if visited[y][right_x] == line:
                    visited[y][right_x] = -1


recursive(0)
print(answer)