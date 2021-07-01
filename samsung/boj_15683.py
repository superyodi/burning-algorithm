import sys, copy, itertools

N, M = map(int,sys.stdin.readline().split(' '))
room = [[0 for _ in range(M)] for _ in range(N)]
tmp_room = []
camera5s = []
cameras = []
spaces = 0
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
cam_dirs = {
    2: ((0, 1), (2,3)),
    3 : ((0, 2), (1,2),(0,3),(1,3)),
    4 : ((3,0,1), (0,1,2), (1,2,3),(2,3,0))
}


def search(coord, dir):
    y, x  = coord
    count = 0

    while True:
        ny = y + dirs[dir][0]
        nx = x + dirs[dir][1]

        if(0<= ny < N and 0<= nx < M):
            if(tmp_room[ny][nx] == 6): return count
            if(tmp_room[ny][nx] == 0):
                tmp_room[ny][nx] = -1
                count += 1

        else: return count
        y, x = ny, nx

    return count



for i in range(N):
    room[i] = list(map(int, sys.stdin.readline().split(' ')))

    for j in range(M):
        if(room[i][j] == 0):
            spaces += 1
        elif(room[i][j] == 5):
            camera5s.append((i,j))
        elif(room[i][j] != 6):
            cameras.append((i,j))

tmp_room = copy.deepcopy(room)

# 5번 카메라 탐색
for camera5 in camera5s:
    count = 0
    for i in range(4):
        count += search(camera5, i)
    spaces -= count

if not cameras:
    print(spaces)
    sys.exit(0)
room = copy.deepcopy(tmp_room)
orders = list(itertools.product(range(4), repeat= len(cameras)))
min_spaces = spaces

while orders:
    order = orders.pop()
    tmp_room = copy.deepcopy(room)
    tmp_spaces = spaces
    count = 0

    for i in range(len(cameras)):
        y, x = cameras[i]
        c_num = tmp_room[y][x]
        dir = order[i]

        if c_num == 1:
            count += search(cameras[i], dir)
        elif c_num == 2:
            count += search(cameras[i], cam_dirs[c_num][dir % 2][0])
            count += search(cameras[i], cam_dirs[c_num][dir % 2][1])

        else:
            for d in range(c_num-1):
                count += search(cameras[i], cam_dirs[c_num][dir][d])

    tmp_spaces -= count
    min_spaces = min(min_spaces, tmp_spaces)
    # print(tmp_spaces)
    # print(order)
    # print(*tmp_room, sep='\n')



print(min_spaces)



