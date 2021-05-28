# https://www.acmicpc.net/problem/3197
# 백조의 호수

import collections, sys

R, C = map(int, sys.stdin.readline().split(" "))

lake = []
times = [[0 for _ in range(C)] for _ in range(R)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

swans = []
visited = [[False for _ in range(C)] for _ in range(R)]
waters = collections.deque()
max_time = 0


# 입력
for i in range(R):
    line = sys.stdin.readline()

    for j in range(C):
        if line[j] == 'L':
            swans.append((i, j))

        if line[j] != 'X':
            waters.append((i, j))
            visited[i][j] = True

    lake.append(list(line[:-1]))


def melt_ice(lake):
    max_time = 0

    while waters:
        y, x = waters.popleft()

        for i in range(4):
            t_y, t_x = y + dy[i], x + dx[i]

            if 0 <= t_y < R and 0 <= t_x < C and visited[t_y][t_x] == False:
                if lake[t_y][t_x] == 'X':
                    times[t_y][t_x] = times[y][x] + 1
                    waters.append((t_y,t_x))
                    visited[t_y][t_x] = True
                    max_time = times[t_y][t_x]

    return max_time

def move_swan(lake, swans, max_num):
    y1, x1 = swans[0]
    y2, x2 = swans[1]


    queue = collections.deque()
    s_visited = [[False for _ in range(C)] for _ in range(R)]

    queue.append((y1, x1))
    s_visited[y1][x1] = True

    while queue:
        y, x = queue.popleft()


        for i in range(4):
            t_y, t_x = y + dy[i], x + dx[i]

            if (t_y, t_x) == (y2, x2):
                return True

            if 0 <= t_y < R and 0 <= t_x < C and s_visited[t_y][t_x] == False:
                if lake[t_y][t_x] == 'L' or lake[t_y][t_x] == '.' or times[t_y][t_x] <= max_num:
                    s_visited[t_y][t_x] = True
                    queue.append((t_y, t_x))

    return False



_min , _max = 0, melt_ice(lake)
answer = _max

while _min <= _max:
    mid = (_min + _max) // 2

    if move_swan(lake, swans, mid):
        _max = mid - 1
        answer = min(answer, mid)

    else:
        _min = mid + 1

print(answer)


