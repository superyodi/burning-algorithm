# 백준 - 최소 환승 경로
import sys, collections

N, L = map(int, sys.stdin.readline().split(" "))

stations = [ [] for _ in range(N+1)]
lines = [ [] for _ in range(L)]

def dfs(start, end):
    visited_lines = [False for _ in range(L)]
    visited_stations = [False for _ in range(N+1)]
    queue = collections.deque()

    for line in stations[start]:
        queue.append([line, start, 0]) # line, station, cnt
        visited_lines[line] = True

    min_cnt = L+1
    while queue:
        line, station, cnt = queue.popleft()
        # print(line, station, cnt)

        if station == end:
            min_cnt = min(min_cnt, cnt)
            continue

        for n_station in lines[line]: # 현재 라인을 지나는 역들, no 환승
            if not visited_stations[n_station]:
                queue.append([line, n_station, cnt])
                visited_stations[n_station] = True

                for n_line in stations[n_station]:
                    if not visited_lines[n_line]:
                        queue.append([n_line, n_station, cnt+1]) # 현재 라인을 지나는 역들 중 환승이 가능한 라인
                        visited_lines[n_line] = True

    if min_cnt == L+1:
        min_cnt = -1
    return min_cnt


for l in range(L):
    line = list(map(int, sys.stdin.readline().split(" ")))

    for s in line:
        if s== -1: break
        lines[l].append(s)
        stations[s].append(l)

start, end = map(int, sys.stdin.readline().split(" "))

print(dfs(start, end))
