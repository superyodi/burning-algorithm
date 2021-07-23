# 백준 - AC

import sys, collections

T = int(sys.stdin.readline())
tc = 0

while tc < T:
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    arr = collections.deque(list(sys.stdin.readline()[1:-2].split(",")))
    r_cnt = 0
    l, r = 0, n-1

    for ch in p:
        if ch == 'R':
            r_cnt += 1
        else:
            if l <= r and r < n:
                if r_cnt % 2 == 1: # R이 홀수번 나올때 -> 뒤집음
                    r -= 1
                else:
                    l += 1
            else:
                print("error")
                break
    else:
        tmp = []
        if r_cnt %2 == 1: #뒤부터 출력
            while l <= r:
                tmp.append(arr[r])
                r -= 1
        else: # 앞부터 출력
            while l <= r:
                tmp.append(arr[l])
                l += 1
        print("["+",".join(tmp)+"]")
    tc += 1