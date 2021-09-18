class Solution:
    def isHappy(self, n: int) -> bool:
        def cal(m):
            total = 0
            while m > 0:
                m, l = divmod(m, 10)  # 몫, 나머지
                total += l ** 2

            return total

        cycles = set()

        while n != 1:
            if n in cycles:
                return False
            cycles.add(n)

            n = cal(n)

        return True