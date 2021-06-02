import math
'''
Runtime: 484 ms, faster than 10.31% of Python3 online submissions for Simplified Fractions.
Memory Usage: 14.6 MB, less than 93.87% of Python3 online submissions for Simplified Fractions.
'''


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        # 분모, 분자
        def check_factor(dnm, mlc):
            # 공약수 찾기
            factor = mlc

            while factor > 1:
                if dnm % factor == 0 and mlc % factor == 0:
                    return True

                factor -= 1

            return False

        if n == 1:
            return []
        answer = []

        # n/m
        for dnm in range(2, n + 1):
            for mlc in range(1, dnm):
                if not check_factor(dnm, mlc):
                    _str = "{0}/{1}".format(mlc, dnm)
                    answer.append(_str)

        return answer


'''
Runtime: 252 ms, faster than 22.28% of Python3 online submissions for Simplified Fractions.
Memory Usage: 14.9 MB, less than 33.43% of Python3 online submissions for Simplified Fractions.
'''
# math gcd 모듈 사용
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        # 분모, 분자

        if n == 1:
            return []
        answer = []

        # n/m
        for dnm in range(2, n + 1):
            for mlc in range(1, dnm):
                if math.gcd(dnm, mlc) == 1:
                    _str = "{0}/{1}".format(mlc, dnm)
                    answer.append(_str)

        return answer
