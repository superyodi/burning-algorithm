# 17. Letter Combinations of a Phone Number

from collections import deque

# [Try 1. Accepted]	28 ms	14.3 MB

# iterate way
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        PN = dict()
        PN['7'] = ['p' ,'q' ,'r' ,'s']
        PN['8'] = ['t', 'u' ,'v']
        PN['9'] = ['w' ,'x' ,'y' ,'z']

        # PN initialate
        n = ord('a')

        for i in range(2, 7):
            i = str(i)
            PN[i] = [chr(n), chr( n +1) ,chr( n +2)]

            n += 3

        before = []
        now = []

        for digit in digits:
            letters = PN[digit][:]

            # 첫 글자
            while before:

                prefix = before.popleft()

                for letter in letters:
                    now.append(prefix + letter)

            if not before:
                if not now:
                    before = collections.deque(letters)

                    if len(digits) == 1:
                        return before
                else:
                    if len(now[0]) == len(digits):
                        return now
                    before = deque(now[:])
                    now.clear()





# [Try 2. Accepted]	20 ms	14.1 MB

# recursive, dfs + backtracking

class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(idx, path):
            if len(path) == len(digits):
                result.append(path)
                return

            # 입력받은 숫자들
            for i in range(idx, len(digits)):
                for j in PN[digits[i]]:
                    dfs(i + 1, path + j)

        if not digits:
            return []

        PN = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
              "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        result = []

        # depth, path
        dfs(0, "")

        return result

