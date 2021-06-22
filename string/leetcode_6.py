class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows < 2:
            return s

        arr = [[] for _ in range(numRows)]

        idx = 0
        dir = True  # 순방, 역방

        for ch in s:
            if idx > numRows - 1:
                idx = numRows - 2
                dir = False

            if idx < 0:
                dir = True
                idx = 1

            arr[idx].append(ch)
            # 순방
            if dir:
                idx += 1
            else:
                idx -= 1

        result = ""
        for _arr in arr:
            result += "".join(_arr)

        return result
