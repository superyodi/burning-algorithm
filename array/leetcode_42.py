# 42. Trapping Rain Water

# [Try 1: Accepted] 100 ms, 15.1 MB

class Solution1:
    def trap(self, height: List[int]) -> int:

        left = 0
        water = 0
        idx = 1

        while idx < len(height):
            if height[idx] >= height[left]:
                water += sum(list(map(lambda x: height[left] - x, height[left:idx])))
                left = idx

            idx += 1

        left += 1

        while left < len(height):
            print(height[left:])
            right = height[left:].index(max(height[left:])) + left
            water += sum(list(map(lambda x: height[right] - x, height[left:right])))

            left = right + 1

        return water

