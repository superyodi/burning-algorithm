# 백준 - 연구소3
import sys
from collections import deque
import copy

N, M = map(int, sys.stdin.readline().split(' '))
room = []
total_virus = []
blnk_cnt = 0
MAX_NUM = 2500
min_time = MAX_NUM
time_temp = [[0 for _ in range(N)] for _ in range(N)]


for i in range(N):
    room.append(list(map(int, sys.stdin.readline().split(' '))))
    for j in range(N):
        if room[i][j] == 2:
            total_virus.append([i, j])
            time_temp[i][j] = '*'
        elif room[i][j] == 0:
            blnk_cnt += 1
        else:
            time_temp[i][j] = '-'


v_visited = [False for _ in range(len(total_virus))]
# 1. dfs(바이러스 선택)
def select_virus(arr):
    global min_time

    if len(arr) == M:
        s_virus = []

        for idx in arr:
            s_virus.append(total_virus[idx])

        # 바이러스 배포, bfs(s_virus)
        # print("let's start")
        time = spread(s_virus)
        min_time = min(time, min_time)
        return

    for i in range(len(total_virus)):
        if not arr or (not v_visited[i] and arr[-1] < i):
            arr.append(i)
            v_visited[i] = True
            select_virus(arr)
            v_visited[i] = False
            arr.pop()



dirs = ((0,-1),(0,1),(1,0),(-1,0))

#2. bfs(바이러스 배포)
def spread(virus):
    now_time = 0
    time_arr = copy.deepcopy(time_temp)

    blnk = blnk_cnt


    for v in virus:
        time_arr[v[0]][v[1]] = 0

    queue = deque(virus)

    while queue:
        x, y = queue.popleft()
        # print(x, y, now_time)
        if blnk == 0: break

        if now_time >= min_time:
            return MAX_NUM

        for dir in dirs:
            nx, ny = x+dir[0], y+dir[1]

            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                if room[nx][ny] == 0 and time_arr[nx][ny] == 0:
                    time_arr[nx][ny] = time_arr[x][y] + 1
                    blnk -= 1
                    now_time = max(time_arr[x][y] + 1, now_time)
                    queue.append([nx, ny])

                elif time_arr[nx][ny] == '*':
                    time_arr[nx][ny] = time_arr[x][y] + 1
                    queue.append([nx, ny])

    # print("result", now_time, blnk)
    # print(*time_arr, sep='\n')
    if blnk != 0:
        return MAX_NUM

    return now_time





select_virus([])

if(min_time == MAX_NUM):
    print(-1)
else:
    print(min_time)


"""
2 2 2 1
2 1 2 2
2 2 1 2
1 2 2 2

4 4
1 1 0 1
0 2 2 0
0 2 2 1
0 1 0 1

4 2
2 2 2 2
2 2 2 2
2 2 2 2
2 2 2 2

11 2
1 1 0 1 1 1 1 1 0 1 1
1 1 2 1 1 1 1 1 2 1 1
0 1 2 1 1 1 0 1 2 1 1
0 1 0 1 1 1 0 1 0 1 1
0 0 2 0 0 1 0 0 2 0 0
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1

답: 4
"""