class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d_nums = {i: nums[i] for i in range(len(nums))}

        for k, v in d_nums.items():
            if v == 1:
                return k



