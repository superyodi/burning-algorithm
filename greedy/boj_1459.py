# 백준 - 걷기

import sys

X, Y, W, S = map(int, sys.stdin.readline().split(" "))

if 2*W <= S: # 대각선보다 직선 2이 더 이득

    sum = (X+Y) * W

elif 2*S < 2*W: # 대각선 2번이 직선 2번보다 이득
    if (X+Y) % 2 == 0: # 대각선만으로 이동
        sum = max(X,Y) * S
    else: # 최대한 대각선으로 이동 후 직선 한번 이동
        sum = (max(X,Y) - 1) * S + W

else: # 직선 2번보단 대각선 한번이 이득
    if X == Y:
        sum = S * X
    else:
        sum = (min(X,Y) * S) + (abs(X-Y) * W)

print(sum)

