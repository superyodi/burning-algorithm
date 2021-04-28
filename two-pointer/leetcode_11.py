# 11. Container With Most Water

# [Try1 : Time Limit Exceeded]

# Brute Force Way ---> 시간초과
class Solution1:
    def maxArea(self, height: List[int]) -> int:

        # 답: 짧은 기둥의 길이 * (기둥2 - 기둥1)

        water = 0

        # 1) Brute Force

        for l in range(len(height) - 1):
            for r in range(l, len(height)):
                water = max(water, (r - l) * min(height[l], height[r]))

        return water


# [Try2 :Accepted]	760 ms	26.6 MB
class Solution2:
    def maxArea(self, height: List[int]) -> int:

        # 답: 짧은 기둥의 길이 * (기둥2 - 기둥1)

        water = 0
        left, right = 0, len(height) - 1

        while left < right:
            water = max(water, (right - left) * min(height[left], height[right]))

            if height[left] <= height[right]:
                left += 1

            else:
                right -= 1

        return water




