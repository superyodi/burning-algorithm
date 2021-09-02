# 백준 - 조합

import sys

n, m = map(int, sys.stdin.readline().split(' '))

m = min(m, n-m)

def combi(k, res):
    # print(k, res)
    if k == m:
        return res * (n - k + 1) // k

    return combi(k + 1, res * (n - k + 1) // k)

if m == 0:
    print(1)

else:
    print(combi(1,1))


