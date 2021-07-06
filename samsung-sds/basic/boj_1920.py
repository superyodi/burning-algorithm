# 백준 - 수 찾기

import sys

N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split(" ")))
arr.sort()

M = int(sys.stdin.readline())
_arr = list(map(int,sys.stdin.readline().split(" ")))
arr2 = sorted(_arr)

f, t = 0, N-1
flag = False
dic = dict()

for target in arr2:

    while f <= t and t < N:
        # print(f, t, target)
        mid = (f+t) // 2
        if arr[mid] == target:
            flag = True
            f = mid
            break

        if arr[mid] < target:
            f = mid + 1
        else:
            t = mid - 1

        flag = False

    if flag:
        dic[target] = 1
        t = N-1
    else:
        dic[target] = 0
        f, t = 0, N-1


for num in _arr:
    print(dic[num])


'''
2
1 2
2
1 2
'''