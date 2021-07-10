
import sys

N, K = map(int, sys.stdin.readline().split(" "))


def fac(k):
    if k == 1:
        return 1
    return k * fac(k-1)
def combi(num, k):
    if k == 1:
        return num
    return num * combi(num-1, k-1)



K = min(N-K, K)

if K == 0:
    print("1")
else:
    print(combi(N, K) // fac(K))
