class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        i = j = 1
        pre = nums[0]

        while i < len(nums):
            if nums[i] != pre:
                nums[j] = nums[i]
                j += 1

            pre = nums[i]
            i += 1

        return j