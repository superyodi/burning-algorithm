# 5. Longest Palindromic Substring (가장 긴 팰린드롬 문자열)

# [try 1: 시간초과 error]

class Solution1:

    def longestPalindrome(self, s: str) -> str:
        # 빠른 return
        def check_palindrom(arr):
            l = 0; r = len(arr)
            flag = True
            while l < r:
                if arr[l] != arr[r]:
                    flag = False
                    break
                l += 1; r -= 1
            return flag



        if len(s) < 2 or s[:] == s[::-1]:
            return s

        s = list(s)
        max_len = 1
        front = 0
        end = len(s)
        answer = s[0]


        while front < len(s):
            if end - front < max_len:
                front += 1
                end = len(s)

                if len(s) - front <= max_len : break

            now = s[front:end]

            # print(now, max_len, answer)

            # 이부분 수정
            if check_palindrom(now):
                if len(now) > max_len:
                    max_len = len(now)
                    answer = "".join(now)

            end -= 1

        # print("답: ",answer)

        return answer



# [try 2: 성공] 8212 ms	14.4 MB
# 1. 문자열 -> 리스트 변환 없이 문자열에서 처리
# 2. while ---> for 변경
class Solution2:

    def longestPalindrome(self, s: str) -> str:

        if len(s) < 2 or s[:] == s[::-1]:
            return s

        # s = list(s)
        max_len = 2
        answer = s[0]

        for l in range(len(s) - 1):

            if len(s) - l < max_len: break
            for r in range(len(s), l, -1):
                if r - l < max_len: break

                if s[l:r] == s[l:r][::-1]:
                    max_len = r - l
                    answer = s[l:r]

                    # print(s[l:r])

        return answer

# [try3: 성공] 8028 ms	14.4 MB
class Solution3:

    def longestPalindrome(self, s: str) -> str:

        if len(s) < 2 or s[:] == s[::-1]:
            return s

        for l in range(len(s) - 1, 1, -1):
            for idx in range(len(s) - l + 1):
                print(s[idx:idx + l])
                if s[idx:idx + l] == s[idx:idx + l][::-1]:
                    print("--------")
                    return s[idx:idx + l]
        print("--------")
        return s[0]



