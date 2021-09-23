# 백준 그룹단어체커

import sys

T = int(sys.stdin.readline())
tc = 0
cnt = 0

while tc < T:
    alphas = set()

    line = sys.stdin.readline().strip()
    pre = ""

    for ch in line:
        if pre != ch and ch in alphas:
            break
        pre = ch
        alphas.add(ch)
    else:
        cnt += 1


    tc += 1

print(cnt)