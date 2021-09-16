# 백준 - 막대기

import sys

X = int(sys.stdin.readline())
arr = []

arr.append(64)
now_sum = 64

while now_sum >= X:
    if now_sum == X:
        print(len(arr))
        break
    now = arr.pop()
    half  = now // 2

    if now_sum - half >= X:
        arr.append(half)
        now_sum -= half
    else:
        arr.append(half)
        arr.append(half)







