import sys, collections



# input data
N, M = map(int, sys.stdin.readline().split(" "))

board = []
blue = []
red = []

# 상, 하, 좌, 우
dy = [-1,1,0,0]
dx = [0,0,-1,1]

# 보드 입력 및 초기화
for n in range(N):
    line = sys.stdin.readline()[:-1]
    for m in range(M):
        if line[m] == 'B':
            blue = [n,m]
        elif line[m] == 'R':
            red = [n,m]

    board.append(line)


def move(board, blue, red, dir):

    # 종료 조건
    # 1. 벽에 부딪힘
    # 2. 구슬이랑 부딪힘
    # 3. 파랑구슬이 구멍에 빠짐
    stop_red, stop_blue = False, False

    while True:
        n_blue = [blue[0]+dy[dir], blue[1]+dx[dir]]
        n_red = [red[0]+dy[dir], red[1]+dx[dir]]

        # 구슬 두개 모두 멈춤
        if stop_blue and stop_red:
            return blue, red

        # 구슬 두개 모두 안멈춤
        elif not stop_red and not stop_blue:
            # 파랑구슬이 구멍에 빠짐
            if board[n_blue[0]][n_blue[1]] == 'O':
                return n_blue, n_red

            # 빨간구슬이 구멍에 빠짐
            if board[n_red[0]][n_red[1]] == 'O':
                stop_red = True
                red = n_red[:]
                continue


            # 벽에 부딪힘
            if board[n_blue[0]][n_blue[1]] == '#':
                stop_blue = True
            if board[n_red[0]][n_red[1]] == '#':
                stop_red = True

            # 둘 다 부딪히지않다면 한칸씩 이동
            if not stop_red and not stop_blue:
                blue, red = n_blue[:], n_red[:]

        # 빨간 구슬만 멈춤
        elif stop_red and not stop_blue:
            if n_blue == red and board[n_blue[0]][n_blue[1]] != 'O':
                return blue, red
            # 파란 구슬도 멈춤
            if board[n_blue[0]][n_blue[1]] == '#':
                return blue, red

            # 파란 구슬 구멍이면
            if board[n_blue[0]][n_blue[1]] == 'O':
                return n_blue, red

            # 파란 구슬 이동 가능하면 한칸 이동
            blue = n_blue[:]

        # 파란 구슬만 멈춤
        elif stop_blue and not stop_red:
            if n_red == blue:
                return blue, red

            # 빨간 구슬도 멈춤
            if board[n_red[0]][n_red[1]] == '#':
                return blue, red

            # 빨간 구슬 구멍이면
            if board[n_red[0]][n_red[1]] == 'O':
                return n_blue, n_red

            # 파란 구슬 이동 가능하면 한칸 이동
            red = n_red[:]



def bfs(board, blue, red):
    queue = collections.deque()
    answer = -1

    visited = set()
    visited.add((blue[0],blue[1],red[0], red[1]))

    queue.append((blue, red, 0))

    while queue:

        inform = queue.popleft()

        # print(inform)
        blue = inform[0]
        red = inform[1]
        count = inform[2]

        if count > 10:
            answer = -1
            break

        if board[red[0]][red[1]] == 'O':
            answer = count
            break

        for i in range(4):

            n_blue, n_red =  move(board, blue, red, i)

            if board[n_blue[0]][n_blue[1]] != 'O' and (n_blue[0], n_blue[1],n_red[0], n_red[1]) not in visited:
                inform = [n_blue, n_red, count + 1]

                queue.append(inform)

                visited.add((n_blue[0], n_blue[1],n_red[0], n_red[1]))


    return answer


# print(*board, sep='\n')
print(bfs(board, blue, red))
