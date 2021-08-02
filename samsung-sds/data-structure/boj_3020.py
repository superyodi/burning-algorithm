# 백준 - 개똥벌레


# [Try1. Brute Force: 시간초과 ]

'''
import sys

N, H = map(int, sys.stdin.readline().split(' '))
crush = {i+1 : 0 for i in range(H)}

for i in range(N):
    num = int(sys.stdin.readline())

    if i%2 == 1: # 석순
        for n in range(1,num+1):
            crush[n] += 1

    else: # 종유석
        for n in range(H, H-num, -1):
            crush[n] += 1

min_val = min(crush.values())
ans = 0
for v in crush.values():
    if v == min_val: ans += 1

print("{} {}".format(min_val, ans))

'''

# [Try2. 누적 합 ]

import sys

N, H = map(int, sys.stdin.readline().split(' '))
crash = [0 for i in range(H + 1)]


for i in range(N):
    num = int(sys.stdin.readline())

    if i%2 == 1: # 석순
        crash[num+1] -= 1
        crash[1] += 1


    else: # 종유석
        num = H - num + 1
        crash[num] += 1

ans = -1
cnt = 0
for i in range(1, H+1):
    crash[i] += crash[i-1]
    if ans == -1 or crash[i] < ans:
        ans = crash[i]
        cnt = 1

    elif crash[i] == ans: cnt += 1



print("{} {}".format(ans, cnt))