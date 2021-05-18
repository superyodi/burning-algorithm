class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1: return 1
        if n == 2: return 2

        arr = [0 for _ in range(n + 1)]

        arr[1] = 1
        arr[2] = 2

        for n in range(3, n + 1):
            arr[n] = arr[n - 1] + arr[n - 2]

        return arr[n]
