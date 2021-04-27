# two pointer를 공부하기 위해 leetcode_3 문제를 다시 풀어봤다.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = dict()
        max_len = 0
        _len = 0
        start = 0

        for idx, ch in enumerate(s):
            if ch not in substr:
                substr[ch] = idx
                _len += 1

            else:
                if substr[ch] < start:
                    substr[ch] = idx
                    _len += 1

                else:
                    max_len = max(max_len, _len)
                    _len = idx - substr[ch]
                    start, substr[ch] = substr[ch] + 1, idx

            # print(start, ch, max_len)

        max_len = max(max_len, _len)

        return max_len