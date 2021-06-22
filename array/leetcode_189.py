# [Try1: Brute Force, 시간초과]
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for _ in range(k):
            num = nums[-1]
            tmp = nums[0]

            for i in range(1, len(nums)):
                nums[i], tmp = tmp, nums[i]

            nums[0] = num

# [Try2: 통과]
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        tmp = [0] * n

        for i in range(n):
            tmp[(i + k) % n] = nums[i]

        nums[:] = tmp
