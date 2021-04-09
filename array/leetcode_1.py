# leetcode, Two Sum


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d_nums = dict()
        for i, k in enumerate(nums):

            if target - k in d_nums:
                return [d_nums[target - k], i]

            d_nums[k] = i

