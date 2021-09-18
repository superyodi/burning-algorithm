# 백준 유레카 이론

import sys, itertools, math

T = int(sys.stdin.readline())
tc = 0
nums = [0] * 1001

for i in range(1, 46):
    for j in range(1, 46):
        for k in range(1, 46):
            tri = i * (i + 1) // 2 + j * (j + 1) // 2 + k * (k + 1) // 2
            if tri <= 1000:
                nums[tri] = 1


while tc < T:
    num = int(sys.stdin.readline())

    print(nums[num])
    tc += 1