#  백준 - 수찾기

import sys

N = sys.stdin.readline().split(' ')
a = list(map(int, sys.stdin.readline().split(' ')))

M = sys.stdin.readline().split(' ')
b = list(map(int, sys.stdin.readline().split(' ')))

a = set(a)

for i in range(len(b)):
    if b[i] in a:
        print(1)
    else: print(0)
