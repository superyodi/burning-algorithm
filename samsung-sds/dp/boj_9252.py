# 백준 - LCS 2
import sys, collections
str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

# 자 맞추기 위해 앞칸 임의로 추가
str1 = '0' + str1
str2 = '1' + str2

dp = [[0 for _ in range(len(str2))] for _ in range(len(str1))]
lcs = collections.deque()


# 처음 값이 변한 숫자를 역추적
def make_lcs(i, j):
    if i <0 or j <0: return

    if dp[i][j] == 0: return

    if dp[i][j] > max(dp[i-1][j], dp[i][j-1]):
        lcs.appendleft(str1[i])
        make_lcs(i - 1, j - 1)

    else:
        return make_lcs(i - 1, j) if dp[i - 1][j] > dp[i][j - 1] else make_lcs(i, j - 1)

for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            if i == 0 or j == 0:
                dp[i][j] =1
            else:
                dp[i][j] = dp[i-1][j-1] + 1

        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


len1 = len(str1) - 1
len2 = len(str2) - 1


make_lcs(len1, len2)

print(len(lcs))

if len(lcs) > 0:
    print("".join(lcs))



'''
ADQWEQWDQWGFSDAHWREYERFGD
FGDGFDSGWERDSAFLSD

9
DGFSWERFD
'''

'''
ASDWADGFRQWE
GHASDQWEZZZZZ

6
ASDQWE
'''