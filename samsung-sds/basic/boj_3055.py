# 백준 - 탈출


# 1. 매 분마다 물이 번지는건 항상 같음
# 2. 고슴도치는 bfs

import sys, collections
# 입력
R, C = map(int, sys.stdin.readline().split(' '))
waters = dict()
waters[0] =set()
arr = []
mole = []
start = ()
dirs = ((-1, 0), (1, 0), (0,-1), (0,1)) # 상, 하, 좌, 우


def water_move(arr, waters):
    new_waters = set()
    for water in waters:
        y, x = water

        for d in dirs:
            ny, nx = y+d[0], x+d[1]

            if 0<= ny < R and 0<= nx < C:
                if arr[ny][nx] != 'D' and arr[ny][nx] != 'X':
                    new_waters.add((ny, nx))

    new_waters = new_waters.union(waters)
    return new_waters



for r in range(R):
    input = list(sys.stdin.readline().strip())
    arr.append(input)
    for c in range(C):
        if arr[r][c] == 'D':
            mole = (r, c)
        elif arr[r][c] == 'S':
            start = (r,c)
        elif arr[r][c] == '*':
            waters[0].add((r, c))

queue = collections.deque()
inform = [start, 0]
queue.append(inform)
min_time = R * C +1
visited = set()

while queue:
    now, time = queue.popleft()
    if now in visited:
        continue
    if time > min_time:
        continue

    visited.add(now)

    if now == mole:
        min_time = min(time, min_time)
        continue

    if time+1 not in waters:
        for t in range(1, time+2):
            if t not in waters:
                waters[t] = water_move(arr, waters[t-1])

    # bfs 시작
    y, x = now
    for d in dirs:
        ny, nx = y + d[0], x + d[1]

        if 0 <= ny < R and 0<= nx < C:
            if arr[ny][nx] == '.' or arr[ny][nx] == 'D':
                if (ny, nx) not in visited and (ny, nx) not in waters[time+1]:
                    queue.append(((ny,nx), time+1))


if min_time == R*C +1:
    print("KAKTUS")
else: print(min_time)


'''
3 3
.D.
.*.
.S*

'''
'''
3 3
***
***
*SD
1
'''

'''
5 7
S....X*
.XXX.X.
..X..X.
X.X.XX.
X...DX.

'''
'''
5 5
.....
..XXD
...XX
S....
....*

'''

'''
10 15
........X......
..XXXXX.X.*....
X.....X.X..*...
.X.S..X.X......
D.X...X.XXXXXXX
.X....X........
.X....X.XXXXXXX
.XXXXXX.X......
........X......
XXXXXXXXX...*..
'''

'''
1 50
S................................................D
->49
--------------------------------------------------------------------

1 50
S..............XD................................*

'''
'''
5 5
*****
XXXXX
*....
S*...
....D
'''

'''
3 3
D..
*..
S*.
'''

'''
3 3
DS.
*X.
...

10 15
........X......
..XXXXX.X.*....
X.....X.X..*...
.X.S..X.X......
D.X...X.XXXXXXX
.X....X........
.X....X.XXXXXXX
.XXXXXX.X......
........X......
XXXXXXXXX...*..
'''