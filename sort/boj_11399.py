# 백준 ATM
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(' ')))

arr.sort()

total = 0
res = 0

for n in arr:
    res += n
    total += res

print(total)