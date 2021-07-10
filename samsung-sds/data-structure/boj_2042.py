# 백준 - 구간 합 구하기

import sys, math

N, M, K = map(int, sys.stdin.readline().split(" "))

arr = []
H = math.ceil(math.log2(N))
TREE_SIZE = 2 ** (H+1)
seg_tree = [0 for _ in range(TREE_SIZE)]

def segment_init(node, start, end):
    # print(node, start, end)
    global seg_tree
    if start == end:
        seg_tree[node] = arr[start]
        return seg_tree[node]

    else:
        seg_tree[node] = segment_init(node*2, start, (start + end)//2)  \
                         +  segment_init(node*2 + 1, (start+end) //2 +1, end)
        return seg_tree[node]

# 전체 범위: [start, end], 구하려는 부분 합: [left, right]
def segment_sum(node, start, end, left, right):
    # case 1. [start, end]와 [left, right]가 아예 겹치지 않는 경우
    if right < start or left > end: return 0
    # case 2. [left, right] 안에 [start, end]가 완전히 포함되는 경우
    if left <= start and end <= right: return seg_tree[node]

    else:
        return segment_sum(node * 2, start, (start + end)//2, left, right) \
               + segment_sum(node * 2+1, (start + end)//2+1, end, left, right)


def segment_update(node, start, end, idx, diff):
    global seg_tree

    if idx < start or idx > end: return

    seg_tree[node] += diff

    if start != end:
        segment_update(node*2, start, (start+end)//2, idx, diff)
        segment_update(node * 2+1,(start + end) // 2+1,end, idx, diff)



# input data
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

# init segment tree
segment_init(1, 0, N-1)


# process command
for _ in range(M+K):
    a, b, c = map(int, sys.stdin.readline().split(" "))

    if a == 1:
        # 숫자 바꾸기
        segment_update(1, 0, N-1, b-1, c- arr[b-1])
        arr[b-1] = c
        pass

    elif a == 2:
        # 부분 합 구하기
        sub_sum = segment_sum(1, 0, N-1,b-1, c-1)
        print(sub_sum)
        pass
