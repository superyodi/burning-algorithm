# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = []

        # 전처리
        for ch in s:
            if ch.isalnum():
                new_s.append(ch.lower())

        f = 0
        t = len(new_s) - 1

        while f < t:
            if new_s[f] == new_s[t]:
                f += 1;
                t -= 1
            else:
                return False

        return True


'''

isalnum() :문자가 숫자, 영어, 한국어일 경우 True
isalpha(): 문자가 영어, 한국어일 경우 True
isdigit(): 문자가 숫자만 있을 경우 True
'''


