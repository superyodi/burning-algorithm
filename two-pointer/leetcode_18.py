# 18. 4Sum

# [Try 1. Accepted]	1132 ms	14.4 MB
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = set()
        # answer에 넣을때 sort해서 넣기

        nums.sort()

        # nums = range(10)

        for a in range(len(nums) - 3):
            for d in range(len(nums) - 1, a + 2, -1):

                # 여기에서 b,c 반복
                b, c = a + 1, d - 1

                while b < c:
                    _sum = nums[a] + nums[b] + nums[c] + nums[d]

                    if _sum < target:
                        b += 1

                    elif _sum > target:
                        c -= 1

                    else:
                        answer.add((nums[a], nums[b], nums[c], nums[d]))
                        # print(a,b,c,d)
                        b += 1
                        c -= 1

        answer = list(map(list, answer))

        return answer