# 백준 암호만들기

import sys

L, C = map(int, sys.stdin.readline().split(' '))

alphas = list(sys.stdin.readline().strip().split(' '))
alphas.sort()
# ['a', 'c', 'i', 's', 't', 'w']

visited = [False] * len(alphas)
mo = {'a', 'e', 'i', 'o','u'}
start = 0

def dfs(word ,idx):

    if len(word) == L:
        if is_valid(word):
            print(word)
        return
    for i in range(idx, C):
        if not visited[i]:
            visited[i] = True
            dfs(word + alphas[i], i)
            visited[i] = False


def is_valid(word):
    cnt_mo = 0
    for al in word:
        if al in mo:
            cnt_mo += 1

    if cnt_mo < 1: return False
    if len(word) - cnt_mo < 2: return False
    return True

dfs("", 0)