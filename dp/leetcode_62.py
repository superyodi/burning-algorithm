class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        if m == 1 or n == 1:
            return 1

        map = [1 for _ in range(n)]

        for y in range(1, m):
            for x in range(1, n):
                map[x] = map[x - 1] + map[x]

        return map[-1]