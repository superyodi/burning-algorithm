# [ 완전탐색 ]
# 백준 - 분해합

import sys

def d_sum(num):
    result = num
    while num > 0:
        num, num2 = divmod(num, 10)
        result+= num2

    return result

N = int(sys.stdin.readline())
M = N - 9 * len(str(N))

ans = 0

while M < N:
    if d_sum(M) == N:
        ans = M
        break
    M += 1


print(ans)