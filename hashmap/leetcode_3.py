# 3. Longest Substring Without Repeating Characters

# [Try 1. 	Time Limit Exceeded]
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_cnt = len(s)

        while max_cnt:
            # 범위 설정
            for i in range(len(s) - max_cnt + 1):
                tmp_s = s[i:i + max_cnt]

                # 중복 확인
                if len(tmp_s) == len(set(tmp_s)):
                    return max_cnt

            max_cnt -= 1

        return 0


'''
tmp 문자열의 범위를 점점 좁히면서 if len(tmp) == len(set(tmp))이면 return하도록 했다
역시나 시간초과
솔루션1의 시간복잡도는 약 ...어후 끔찍하다 심지어 set(tmp_s)가 O(N)인데 이걸 N 안에서 N번 돌도록하다니....
약 O(N^3)
'''

# [Try2. Accepted]	60 ms	14.4 MB
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ch_dict = dict()
        max_count = 0
        start = 0

        for i, ch in enumerate(s):
            # keep going하면서 시작 위치 update
            if ch not in ch_dict:
                ch_dict[ch] = i

            else:
                start = max(ch_dict[ch] + 1, start)
                ch_dict[ch] = i

            # max_cnt update
            max_count = max(max_count, i - start + 1)

        return max_count


'''
머리를 쓰자 
문자열 하나를 쭉 지나는동안 겹치는 문자를 발견했다면 그 문자가 원래 있던 idx의 한칸 뒤부터 start지점을 다시 새워두도록했다
만약 start가 겹치는 문자보다 뒤라면 start 변동이 없어야하므로 start = max(start, ch_dict[ch] + 1)

'''