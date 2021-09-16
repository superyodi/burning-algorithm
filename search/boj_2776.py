# 백준 - 암기왕

import sys

T = int(sys.stdin.readline())

tc = 0
while tc < T:
    N = int(sys.stdin.readline())
    arr1 = list(map(int, sys.stdin.readline().split(' ')))
    arr1.sort()

    M = int(sys.stdin.readline())
    arr2 = list(map(int, sys.stdin.readline().split(' ')))

    for pivot in arr2:
        l, r = 0, len(arr1)
        flag = False

        while l < r:
            m = (l + r) // 2
            if arr1[m] == pivot:
                flag = True
                break

            elif arr1[m] < pivot:
                l = m + 1
            else:
                r = m

        print(int(flag))

    tc += 1
