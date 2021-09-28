# 백준 좋은 수열
import sys

N = int(sys.stdin.readline())

nums = ['1','2','3']
result = ""

def backtracking(res):
    global result
    if len(result) != 0: return
    if not is_valid(res): return
    if len(res) == N:
        result = res
        return
    for num in nums:
        if is_valid(res + num):
            backtracking(res + num)

def is_valid(s):
    r = len(s) -1
    l = r -1
    size = 1
    while l >= 0:
        if s[l:l+size] == s[r:r+size]:
            return False
        size += 1
        l -= 2
        r -= 1
    return True


backtracking("")
print(result)