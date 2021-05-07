
def solution(board):
    answer = 0

    # dfs 알고리즘

    # 홀수 idx -> 수직이동, 짝수 idx -> 수평이동
    direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # 직선 100, 코너 500
    def dfs(y, x, cost, dir):

        if y < 0 or y > len(board) - 1 or x < 0 or x > len(board) - 1:
            return
        if board[y][x]:
            return

        if cost > map[y][x] and map[y][x] != 0:
            return

        else:

            map[y][x] = cost

            for _dir in range(len(direct)):
                # 방향이 같을때, 100원만 추가

                if x == len(board) - 1 and y == len(board) - 1:
                    dfs(y + direct[_dir][0], x + direct[_dir][1], cost + 100, _dir)

                elif _dir % 2 == dir % 2:
                    dfs(y + direct[_dir][0], x + direct[_dir][1], cost + 100, _dir)

                else:
                    dfs(y + direct[_dir][0], x + direct[_dir][1], cost + 600, _dir)

            if y == len(board) - 1 and x == len(board) - 1:
                print(map[y][x])

    map = [[0] * len(board) for _ in range(len(board))]

    end = len(board) - 1

    dfs(end, end, 0, 0)

    return map[0][0]


'''
통과는 했지만 반례 있음

board = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 1, 0, 0]]



'''


# 반례 해결, 하지만 시간초과
def solution(board):
    # dfs 알고리즘

    # 홀수 idx -> 수직이동, 짝수 idx -> 수평이동
    direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # 직선 100, 코너 500
    def dfs(y, x, cost, dir):

        if y < 0 or y > len(board) - 1 or x < 0 or x > len(board) - 1:
            return
        if board[y][x]:
            return

        if cost > map[y][x][dir] and map[y][x][dir] != 0:
            return
        else:

            map[y][x][dir] = cost

            for _dir in range(len(direct)):
                # 방향이 같을때, 100원만 추가

                if x == 0 and y == 0:
                    dfs(y + direct[_dir][0], x + direct[_dir][1], cost + 100, _dir % 2)

                elif _dir % 2 == dir % 2:
                    dfs(y + direct[_dir][0], x + direct[_dir][1], cost + 100, _dir % 2)

                else:
                    dfs(y + direct[_dir][0], x + direct[_dir][1], cost + 600, _dir % 2)

    map = [[[0, 0] for _ in range(len(board))] for _ in range(len(board))]

    end = len(board) - 1

    dfs(0, 0, 0, 0)

    tmp1, tmp2 = map[end][end]

    if tmp1 == 0:
        return tmp2

    if tmp2 == 0:
        return tmp1

    return min(tmp1, tmp2)

# bfs, 하지만 답 안맞음
def solution(board):
    directs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    map = [[[0, 0] for _ in range(len(board))] for _ in range(len(board))]

    queue = [[0, 0, 0], [0,0,1]]

    while queue:
        y, x, d = queue.pop(0)

        print((y,x,d),map[y][x][d])

        # idx%2 == 0 ---> 수직이동, idx%2 == 1 ----> 수평이동
        for idx, dir in enumerate(directs):
            n_y, n_x, n_d = y+dir[0], x+dir[1], idx%2

            if n_y < 0 or n_y >= len(board) or n_x < 0 or n_x >= len(board):
                continue

            if board[n_y][n_x]:
                continue

            if d == n_d:
                if map[n_y][n_x][n_d] == 0 or map[y][x][d] + 100 < map[n_y][n_x][n_d]:
                    map[n_y][n_x][n_d] = map[y][x][d] + 100
                    queue.append([n_y, n_x, n_d])
            else:
                if map[n_y][n_x][d] == 0 or map[y][x][d] + 600 < map[n_y][n_x][d]:
                    map[n_y][n_x][d] = map[y][x][d] + 600
                    queue.append([n_y, n_x, d])

    print(map)




    end = len(board) - 1



    #     tmp1, tmp2 = map[end][end]

    #     if tmp1 == 0:
    #         return tmp2

    #     if tmp2 == 0:
    #         return tmp1

    # return min(tmp1, tmp2)

    return 0

tc1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
tc2 = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
# 2100

print(solution(tc2))