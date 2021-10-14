# 백준 사다리 조작


import sys

# 세로, 가로, 가로선 갯
N, M, H = map(int , sys.stdin.readline().split(' '))

maps = {i : set() for i in range(1, N+1)}

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split(' '))
    maps[b].add(a)

flag = False
res = 4
history = []

def dfs(now, cnt, nxt):

    global res, flag
    # if flag: return
    if cnt >= res: return
    if now == N:
        # 사다리 타기

        for c_start in range(1, N+1):
            r, c = 1, c_start

            while r < H+1:
                # print(r, c)
                if r in maps[c]:
                    c += 1
                    r += 1
                    continue

                if c > 1 and r in maps[c-1]:
                    c -= 1
                    r += 1
                    continue
                r += 1

            if c != c_start: break
        else:
            flag = True
            res = min(res, cnt)
        #     print("성공")
        # print(maps)
        return

    if len(maps[now]) != 1: dfs(now+1, cnt, 0)

    for nxt in range(nxt+1, H+1):
        if nxt not in maps[now]:
            if (now < N and nxt in maps[now+1]) or (now > 1 and nxt in maps[now-1]):
                continue

            maps[now].add(nxt)
            dfs(now, cnt+1, nxt+1)
            maps[now].remove(nxt)


dfs(1, 0, 0)

if flag and res < 4:
    print(res)
else:
    print(-1)

