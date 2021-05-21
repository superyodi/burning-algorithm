# 15. 3Sum

# [Try 1: Time Limit Exceeded]

from itertools import combinations


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) < 3:
            return []
        nCr = combinations(nums, 3)
        nCr = list(nCr)

        answers = set()

        while nCr:
            three_sum = list(nCr.pop())

            if sum(three_sum) == 0:
                three_sum.sort()
                answers.add(tuple(three_sum))

        answers = list(map(lambda x: list(x), answers))

        return answers


# [Try 2: Accepted] 1832 ms 16.7 MB
from itertools import combinations


class Solution2(object):
    def threeSum(self, nums):

        d_nums = dict()
        answers = dict()

        for n in nums:
            if n in d_nums:
                d_nums[n] += 1
            else:
                d_nums[n] = 1

        nums = list(set(nums))

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                x, y = nums[i], nums[j]
                x_cnt, y_cnt = d_nums[x], d_nums[y]

                d_nums[x] -= 1;

                if d_nums[y] < 1:
                    continue
                d_nums[y] -= 1

                z = - (x + y)

                if z in d_nums and d_nums[z] > 0:
                    # print(x,y,z)
                    three_sum = tuple(sorted([x, y, z]))
                    if three_sum not in answers:
                        answers[three_sum] = True

                d_nums[x], d_nums[y] = x_cnt, y_cnt

        answers = answers.keys()

        return answers


