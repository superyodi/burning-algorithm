
# 백준 후보 추천하기

import sys

N = int(sys.stdin.readline())
total = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().strip().split(" ")))

pic_dic = dict()

for idx, num in enumerate(nums):
    if num in pic_dic:
        pic_dic[num][0] += 1
        continue

    if len(pic_dic) == N:
        del_num = sorted(pic_dic.items(), key= lambda x: x[1])[0][0]
        del(pic_dic[del_num])

    pic_dic[num] = [1, idx]



answer = list(map(str, sorted(pic_dic.keys())))
answer = " ".join(answer)
print(answer)


'''
3
14
2 1 4 3 5 6 2 7 2 100 100 54 54 50
'''