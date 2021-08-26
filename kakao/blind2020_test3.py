# 자물쇠와 열쇠


import copy

def solution(key, lock):
    lock, lock_cnt = padding(lock)

    for i in range(4):
        # print(i, "번째 회전")
        result = move(key, lock, lock_cnt)
        if result:
            return True
        key = rotate(key)

    return False


def rotate(old):
    new = copy.deepcopy(old)

    end = len(old) - 1
    for i in range(len(old)):
        for j in range(len(old)):
            new[j][end - i] = old[i][j]

    return new

def padding(old):
    size = len(old)
    new = [[1 for _ in range(3*size) ]for _ in range(3*size)]
    lock_cnt = 0
    for i in range(size):
        for j in range(size):
            if old[i][j] == 0: lock_cnt += 1
            new[i+size][j+size] = old[i][j]

    return new, lock_cnt

def move(key, lock, lock_cnt):

    for i in range(len(lock)):
        for j in range(len(lock)):

            if lock_cnt == match(key,lock, i, j):
                return True

    return False

def match(key, lock, s_i, s_j):
    l_size = len(lock) // 3

    # print(f"l_size: {l_size}, s_i: {s_i}, s_j: {s_j}")

    if l_size * 2 <= s_i or l_size * 2 <= s_j or \
        s_i + len(key) <= l_size or s_j + len(key) <= l_size:
        # print("out of range")
        return -1

    cnt = 0
    for i in range(len(key)):
        for j in range(len(key)):
            l_i, l_j = s_i+ i, s_j + j
            if l_i < l_size or l_j < l_size or l_i >= l_size*2 or l_j >= l_size*2:
                continue

            if key[i][j] ^ lock[l_i][l_j]:
                if key[i][j] == 1 and lock[l_i][l_j] == 0:
                    cnt += 1
            else: return -1
    return cnt







'''
sliding window 문제인것 같다.
통크게 len(lock) * 3 으로 새 배열을 할당한 후 가운데 lock을 두고
brute force하면서 완전탐색 하자 

2차원배열을 자유자재로 다룰 수 있는지 확인하는 용도의 문제  


'''