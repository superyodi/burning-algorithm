# 주사위 굴리기

import sys

N, M, y, x, K = map(int,sys.stdin.readline().split(' '))
d_map = []
dice = [0 for i in range(7)]


# 동, 서, 북, 남
dirs = [(0,0), (0,1),(0,-1),(-1,0),(1,0)]


for i in range(N):
    line = sys.stdin.readline()[:-1].split(' ')
    line = list(map(int,line))

    d_map.append(line)

cmds = list(map(int,list(sys.stdin.readline().split(' '))))

# 북쪽, 정면, 동쪽
now = [1,5,3]

for cmd in cmds:
    dir = dirs[cmd]

    ny = y + dir[0]
    nx = x + dir[1]

    # 이동 가능성 확인
    if (0<= ny < N and 0 <= nx < M):
        # 동
        next = []
        if cmd == 1:
            # 북쪽, 정면, 동쪽
            next = [7-now[2],now[1], now[0]]
        # 서
        elif cmd == 2:
            next = [now[2], now[1], 7-now[0]]
        # 북
        elif cmd == 3:
            next = [now[1], 7-now[0],now[2]]
        # 남
        else:
            next = [7-now[1], now[0], now[2]]

        # print(next)
        top = next[0]
        bottom = 7 - top

        print(dice[top])

        if d_map[ny][nx] == 0:
            #  이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다.
            d_map[ny][nx] = dice[bottom]

        else:
            # 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
            dice[bottom], d_map[ny][nx] = d_map[ny][nx], 0

        y, x = ny, nx
        now = next[:]



