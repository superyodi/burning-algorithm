# 77. Combinations

# 조합의 정의: 순서상관없이 n개 중 k개를 뽑아서 나열
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        answer = []

        def dfs(elements, start, k):

            if k == 0:
                answer.append(elements[:])
                return

            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)

        return answer

