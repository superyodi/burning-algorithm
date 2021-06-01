import sys, collections

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

board = [[0 for _ in range(N+1)] for _ in range(N+1)] # snake board
d_rotate = dict() # 방향 정보 딕셔너리
snake = collections.deque([[1,1]])
time = 1
# 우, 하, 좌, 상
dirs = [[0,1],[1,0],[0,-1],[-1,0]]

for _ in range(K):
    y, x = map(int, sys.stdin.readline().split(' '))
    # 사과는 2로 표시
    board[y][x] = 2

L = int(sys.stdin.readline())
for _ in range(L):
    k, v = sys.stdin.readline().strip().split(' ')
    d_rotate[int(k)] = v


# dirction
d = 0
board[1][1] = 1

while 1:
    # print(time)
    # print(*board, sep='\n')
    head = snake[-1]
    head = [x+y for x,y in zip(head, dirs[d])]

    if 1<= head[0] < N+1 and 1<= head[1] < N+1:
        # 뱀의 몸통
        if board[head[0]][head[1]] == 1:
            break
        # 사과가 없을때 꼬리부분 삭제
        if board[head[0]][head[1]] == 0:
            tail = snake.popleft()
            board[tail[0]][tail[1]] = 0

        board[head[0]][head[1]] = 1
        snake.append(head)

    # board의 경계를 넘었을때 break
    else: break

    if time in d_rotate:
        if d_rotate[time] == 'D':
            d = (d + 1) % 4
        if d_rotate[time] == 'L':
            d = (d - 1) % 4

    time += 1

print(time)
