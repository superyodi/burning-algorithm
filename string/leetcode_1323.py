# [Try 1 : Accepted]
# Your runtime beats 5.05 % of python3 submissions.

class Solution:
    def maximum69Number(self, num: int) -> int:
        num = list(str(num))
        for i in range(len(num)):

            if num[i] == '6':
                num[i] = '9'
                break

        return "".join(num)


# [Try 2 : Accepted]
# Your runtime beats 53.23 % of python3 submissions.


class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))



'''
교훈: 파이썬 라이브러리를 애용하자 

str.replace(old, new[, count])
모든 부분 문자열 old 가 new 로 치환된 문자열의 복사본을 돌려줍니다. 선택적 인자 count 가 주어지면, 앞의 count 개만 치환됩니다.

'''