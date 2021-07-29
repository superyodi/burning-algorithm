# 백준 - 적록색약


import sys, collections

N = int(sys.stdin.readline())

# Brute Force
arr = []
for _ in range(N):
    line = sys.stdin.readline().strip()
    arr.append(line)


visited_pos = [[False for _ in range(N)] for _ in range(N)]  # 적록색약 양성
visited_neg = [[False for _ in range(N)] for _ in range(N)]  # 적록색약 음성

def bfs(start, flag):

    dirs = ((-1,0),(1,0),(0,1),(0,-1)) # 상하우좌
    queue = collections.deque()
    queue.append(start)

    while queue:
        y, x = queue.popleft()

        if flag: # 양성일때
            if visited_pos[y][x]:
                continue
            visited_pos[y][x] = True
        else:
            if visited_neg[y][x]:
                continue
            visited_neg[y][x] = True

        for dir in dirs:
            ny, nx = y+dir[0], x+dir[1]

            if 0<=ny<N and 0<=nx<N:
                if arr[y][x] == arr[ny][nx]: # 같은 알파벳일때
                    if flag:
                        if not visited_pos[ny][nx]:
                            queue.append((ny,nx))
                    else:
                        if not visited_neg[ny][nx]:
                            queue.append((ny,nx))

                elif flag:
                    if arr[y][x] == 'R' and arr[ny][nx] == 'G':
                        if not visited_pos[ny][nx]:
                            queue.append((ny, nx))

                    elif arr[y][x] == 'G' and arr[ny][nx] == 'R':
                        if not visited_pos[ny][nx]:
                            queue.append((ny, nx))

cnt_neg, cnt_pos = 0, 0
# 적록색약 아닐때 카운트
for y in range(N):
    for x in range(N):
        if not visited_neg[y][x]:
            cnt_neg += 1
            bfs((y,x), False)

# 적록색약일 카운트
for y in range(N):
    for x in range(N):
        if not visited_pos[y][x]:
            cnt_pos += 1
            bfs((y, x), True)

print("{} {}".format(cnt_neg, cnt_pos))

