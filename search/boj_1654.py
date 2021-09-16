# 백준 - 랜선 자르기
# b-search

import sys

K, N = map(int, sys.stdin.readline().split(' '))
max_lan = 0
lans = []
for _ in range(K):
    lan = int(sys.stdin.readline())
    max_lan = max(max_lan, lan)
    lans.append(lan)

left = 1
right = max_lan

while left <= right:
    # cut
    mid = (left + right) // 2

    cnt = 0
    for lan in lans:
        cnt += (lan // mid)

    if cnt > (N-1):
        left = mid+1

    else: right = mid-1

print(left-1)


