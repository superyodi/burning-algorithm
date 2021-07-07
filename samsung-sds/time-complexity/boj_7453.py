# 백준 - 합이 0인 4 정수

import sys


# [Try 1.] lower-bound, upper-bound로 했지만 시간초과~~~
# 파이썬만 유난이고 c++에서는 돌아감

'''
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    line = list(map(int ,sys.stdin.readline().split(' ')))
    arr.append(line)


ab_list = []
cd_list = []

# val이 나오는 첫번째 위치
def lower_bound(arr, val):
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < val:
            left = mid+1
        else:
            right = mid-1

    if arr[left] != val: return -1
    return left

# val이 끝나는 첫번째 위치
def upper_bound(arr, val):
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left + right) // 2
        # print(mid, arr[mid])
        if arr[mid] <= val:
            left = mid+1
        else:
            right = mid-1
    return right+1


for i in range(n):
    for j in range(n):
        ab = arr[i][0] + arr[j][1]
        ab_list.append(ab)

        cd = arr[i][2] + arr[j][3]
        cd_list.append(cd)


cd_list = sorted(cd_list)

left, right = 0, len(cd_list)-1
count = 0

for ab in ab_list:
    # 해당 값이 존재할때
    lower_idx = lower_bound(cd_list, -ab)

    if lower_idx != -1:
        count += upper_bound(cd_list, -ab) - lower_bound(cd_list, -ab)

print(count)
'''


# [Try 2. ] 딕셔너리로 착착착 --> 역시 시간초과, 파이썬은 답이 없다

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    line = list(map(int ,sys.stdin.readline().split(' ')))
    arr.append(line)


ab_dict = dict()
cd_dict = dict()

for i in range(n):
    for j in range(n):
        ab = arr[i][0] + arr[j][1]
        cd = arr[i][2] + arr[j][3]
        if ab not in ab_dict:
            ab_dict[ab] = 1
        else:
            ab_dict[ab] += 1

        if cd not in cd_dict:
            cd_dict[cd] = 1
        else:
            cd_dict[cd] += 1


answer = 0
for _, k in enumerate(ab_dict):
    if cd_dict.get(-k):
        answer += cd_dict[-k] * ab_dict[k]

print(answer)



'''
10
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0

'''