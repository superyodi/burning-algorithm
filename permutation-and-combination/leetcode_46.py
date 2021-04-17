# 순열 직접 구현해보기. 증말 생각보다 쉽지않다

# 46. Permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        pre_elements = []

        def dfs(elements):
            if len(elements) == 0:
                results.append(pre_elements[:])

            for el in elements:
                next_elements = elements[:]
                next_elements.remove(el)

                pre_elements.append(el)
                dfs(next_elements)
                pre_elements.pop()

        dfs(nums)
        return results

'''
한동안 붙잡고있다가 gg치고 파알인 저자의 코드를 고대로 가져온건데 아름답다
어떻게 저렇게 컴팩트한 코드를 짤 수 있을까?

'''
