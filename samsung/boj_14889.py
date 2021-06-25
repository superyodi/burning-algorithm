# 스타트와 링크

import itertools

N = int(input())
board = []
_sum = 0
for _ in range(N):
    line = list(map(int,input().split(' ')))
    _sum += sum(line)
    board.append(line)

combi = list(itertools.combinations(range(N), N//2))
start = 0
link = len(combi) - 1

min_gap = _sum

while start < len(combi) // 2:
    now = combi[start]
    _now = combi[link]


    start_sum = 0
    link_sum = 0

    for i in range(len(now)-1):
        for j in range(i+1, len(now)):
            s_i, s_j = now[i], now[j]
            l_i, l_j = _now[i], _now[j]

            start_sum += board[s_i][s_j]
            start_sum += board[s_j][s_i]

            link_sum += board[l_i][l_j]
            link_sum += board[l_j][l_i]

    gap = abs(start_sum - link_sum)
    min_gap = min(min_gap, gap)

    start += 1
    link -= 1


print(min_gap)

