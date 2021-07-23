# 백준 - 광고
# KMP
import sys
def make_lps(p):
    lps = [0] * len(p)
    pre, now = 0, 1

    while now < len(p):
        if p[now] == p[pre]:
            pre += 1
            lps[now] = pre
            now += 1

        else:
            if pre != 0:
                pre = lps[pre-1]
            else:
                lps[now] = 0
                now +=1

    return lps

L = int(sys.stdin.readline())
p = sys.stdin.readline().strip()

if len(p) == 1:
    print("1")
else:
    lps = make_lps(p)
    # print(lps)
    answer = len(lps) - lps[-1]
    print(answer)
