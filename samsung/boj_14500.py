# 테트로미노

import sys, collections

N, M = map(int,sys.stdin.readline().split(' '))

paper = []
visited = [[0 for _ in range(M)] for _ in range(N)]

max_sum = 0
# 왼쪽, 오른쪽, 아래
dirs = [(0,-1),(0,1),(1,0)]


for i in range(N):
    line = list(map(int,sys.stdin.readline().split(' ')))
    paper.append(line)


def sum_blocks(paper, blocks):
    _sum = 0

    for block in blocks:
        y, x = block
        _sum += paper[y][x]

    return _sum


def calc_block(paper, now, now_sum, visited):
    global max_sum
    if len(visited) == 4:
        max_sum = max(max_sum, now_sum)
        return

    for dir in dirs:
        ny, nx = now[0] + dir[0], now[1] + dir[1]

        if 0<=ny <N and 0<=nx < M:
            if (ny,nx) not in visited:
                _visited = visited.copy()
                _visited.add((ny, nx))
                calc_block(paper, (ny,nx), now_sum+ paper[ny][nx], _visited)



# T자형 블럭일때
def calc_t_block(paper, now, now_sum):

    global max_sum

    y, x = now

    # 상 ㅜ
    if 0<= y-1 <N and 0<= x-1 < M and 0<= x+1 <M:
        side_sum = 0
        side_sum += paper[y - 1][x - 1]
        side_sum += paper[y - 1][x]
        side_sum += paper[y - 1][x + 1]

        max_sum = max(max_sum, now_sum + side_sum)


    # 하 ㅗ
    if 0 <= y + 1 < N and 0 <= x - 1 < M and 0 <= x + 1 < M:
        side_sum = 0
        side_sum += paper[y + 1][x - 1]
        side_sum += paper[y + 1][x]
        side_sum += paper[y + 1][x + 1]

        max_sum = max(max_sum, now_sum + side_sum)

    # 좌 ㅏ
    if  0 <= x - 1 < M and 0<= y-1 <N and 0<= y+1 <N:
        side_sum = 0
        side_sum += paper[y - 1][x - 1]
        side_sum += paper[y][x - 1]
        side_sum += paper[y + 1][x - 1]

        max_sum = max(max_sum, now_sum + side_sum)

    # 우 ㅓ
    if  0 <= x + 1 < M and 0<= y-1 <N and 0<= y+1 <N:
        side_sum = 0
        side_sum += paper[y - 1][x + 1]
        side_sum += paper[y][x + 1]
        side_sum += paper[y + 1][x + 1]

        max_sum = max(max_sum, now_sum + side_sum)

    return

for n in range(N):
    for m in range(M):
        calc_t_block(paper, (n,m), paper[n][m])

        _visited = set()
        _visited.add((n,m))
        calc_block(paper, (n,m), paper[n][m], _visited)




print(max_sum)


