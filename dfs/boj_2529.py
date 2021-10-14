# 백준 부등호

import sys

k = int(sys.stdin.readline())
inputs = sys.stdin.readline().strip().split(' ')
nums = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
visited = [False] * 10
flag = False


def min_num(arr, size):
    global flag

    if flag: return
    if size == k+1:
        print("".join(map(str, arr)))
        flag = True
        return

    for i in range(10):
        if not visited[i]:

            if not arr:
                arr.append(i)
                visited[i] = True
                min_num(arr, size + 1)
                visited[i] = False
                arr.pop()

            else:

                if inputs[size-1] == '>':
                    if arr[-1] > i:
                        arr.append(i)
                        visited[i] = True
                        min_num(arr, size+1)
                        visited[i] = False
                        arr.pop()

                else:
                    if arr[-1] < i:
                        arr.append(i)
                        visited[i] = True
                        min_num(arr, size + 1)
                        visited[i] = False
                        arr.pop()


def max_num(arr, size):
    global flag

    if flag: return
    if size == k+1:
        print("".join(map(str, arr)))
        flag = True
        return

    for i in range(9,-1,-1):
        if not visited[i]:

            if not arr:
                arr.append(i)
                visited[i] = True
                max_num(arr, size + 1)
                visited[i] = False
                arr.pop()

            else:

                if inputs[size-1] == '>':
                    if arr[-1] > i:
                        arr.append(i)
                        visited[i] = True
                        max_num(arr, size+1)
                        visited[i] = False
                        arr.pop()

                else:
                    if arr[-1] < i:
                        arr.append(i)
                        visited[i] = True
                        max_num(arr, size + 1)
                        visited[i] = False
                        arr.pop()


max_num([], 0)
flag = False
min_num([],  0)
