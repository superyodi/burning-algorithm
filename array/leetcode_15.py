# 15. 3Sum

# [Try 1: Accepted] Time Limit Exceeded

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




# 풀다말았음
class Solution2:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        d_nums = {
            nums[-1]: set(len(nums) - 1)
        }
        answers = set()

        for i in range(len(nums) - 1):

            if nums[i] in d_nums:
                d_nums[num[i]].add(i)
            else:
                nums[i] = set(i)

            for j in range(i + 1, len(nums)):
                x, y = nums[i], nums[j]
                z = - (x + y)

                if z in s_nums:
                    # print(x,y,z)
                    three_sum = tuple(sorted([x, y, z]))
                    answers.add(three_sum)

        answers = list(map(lambda x: list(x), answers))

        return answers



