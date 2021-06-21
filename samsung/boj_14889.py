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

visited = set()
min_gap = _sum

while combi:
    now = combi.pop()
    _now = tuple(filter(lambda x: x not in now, range(N)))

    if now in visited or _now in visited:
        continue
    # print(now, _now)

    visited.add(now)
    visited.add(_now)

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


print(min_gap)

