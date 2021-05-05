# [Try 1. Passed] Sorting
# O(nlogn)

class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        nums.sort()

        pre = nums[0]
        count = 0
        max_count = 0

        for i in range(1, len(nums)):
            if nums[i] == pre + 1:
                count += 1

            elif nums[i] == pre:
                continue

            else:
                max_count = max(max_count, count)
                count = 0

            pre = nums[i]

        max_count = max(max_count, count) + 1
        return max_count

# [Try 2. Passed] union-find
# 어떻게 이런 방법이,,,,ㄷ,,ㄷ,,
# O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        max_len = 0

        for num in nums:
            if num - 1 not in nums:
                now = num
                now_len = 1

                while now + 1 in nums:
                    now += 1
                    now_len += 1

                max_len = max(max_len, now_len)

        return max_len

