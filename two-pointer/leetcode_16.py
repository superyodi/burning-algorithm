# 16. 3Sum Closest

# [Try1. Time Limit Exceeded]

# 조합을 이용했지만 실패
# O(N^3)

import itertools

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # nums.sort()
        # print(nums)

        # 1. 조합 사용
        nC3 = list(itertools.combinations(nums, 3))

        nC3 = list(map(lambda x: sum(x), nC3))

        min_sum = [10 ** 3, -1]

        for c in nC3:
            if abs(target - c) < min_sum[0]:
                min_sum = [abs(target - c), c]

        return min_sum[1]


# [Try2. Accepted]	332 ms	14.3 MB

# two pointer를 사용해서 해결
# O(N^2)

class Solution2:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        # [_gap, _sum]
        min_gap = [10 ** 4, 1]

        # low 를 위한 for문
        for low in range(len(nums) - 2):
            now, high = low + 1, len(nums) - 1

            while now < high:

                _sum = nums[low] + nums[now] + nums[high]
                _gap = abs(target - _sum)

                if _gap < min_gap[0]:
                    min_gap = [_gap, _sum]

                if _sum < target:
                    now += 1

                else:
                    high -= 1

        # print(min_gap)
        return min_gap[1]





