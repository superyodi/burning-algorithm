# 연구소


import sys, itertools, collections, copy

def spread_virus(lab, virus, walls, cnt_blanks):

    l_map = copy.deepcopy(lab)
    # stand walls in lab
    for wall in walls:
        y, x = wall
        l_map[y][x] = 1

    cnt_blanks -= 3

    visited = [[False for _ in range(M) ]for _ in range(N)]
    # 상,하,좌,우
    dirs= [(-1,0), (1,0),(0,-1),(0,1)]

    queue = collections.deque(virus)

    # spread virus
    while queue:
        y, x = queue.popleft()


        if visited[y][x]:
            continue
        visited[y][x] = True

        if l_map[y][x] == 0:
            l_map[y][x] = 2
            cnt_blanks -= 1

        for dir in dirs:
            dy, dx = y+ dir[0], x+dir[1]

            if 0<= dy<N and 0<=dx<M:
                if l_map[dy][dx] != 1 and not visited[dy][dx]:
                    queue.append((dy,dx))

    return cnt_blanks




# 지도 입력받음
N, M = map(int, sys.stdin.readline().split(' '))

lab = [[0 for _ in range(M)] for _ in range(N)]
virus = []
blanks = []
cnt_blanks = 0

for n in range(N):
    line = sys.stdin.readline().split(' ')

    for m in range(M):
        lab[n][m] = int(line[m])

        if lab[n][m] == 2:
            virus.append((n,m))

        elif lab[n][m] == 0:
            blanks.append((n,m))
            cnt_blanks += 1

combi = list(itertools.combinations(blanks, 3))

max_count = 0

for walls in combi:


    now_count = spread_virus(lab, virus, walls, cnt_blanks)
    max_count = max(max_count, now_count)


print(max_count)

