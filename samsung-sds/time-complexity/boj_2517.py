# 백준 - 달리기

# 하지만 시간초과

import sys

# input
N = int(sys.stdin.readline())
runners = []
sg_tree = [0 for _ in range(2 ** 20)]


def segment_sum(node, s, e, l, r):
    if r < s or e < l: return 0
    if l <= s and e <= r:
        return sg_tree[node]
    else:
        return segment_sum(node * 2, s, (s + e) // 2, l, r)  \
               + segment_sum(node * 2 + 1, (s + e) // 2 + 1, e, l, r)


def update(node, s, e, idx, val):
    global sg_tree
    if idx < s or e < idx: return
    if s == e:
        sg_tree[node] = val
    else:
        update(node * 2, s, (s + e) // 2, idx, val)
        update(node * 2 + 1, (s + e) // 2 + 1, e, idx, val)
        sg_tree[node] = sg_tree[node * 2] + sg_tree[node * 2 + 1]


for i in range(N):
    runners.append([i, int(sys.stdin.readline())])

# re-labeling : 능력치를 내림차순순으로 라벨링해서 다시 값 넣어줌
runners.sort(key=lambda x: x[1])


for i in range(N):
    runners[i][1] = i + 1

# 다시 sort: original order
runners.sort()

for i in range(N):
    now_power = runners[i][1]
    count = 0

    # 제일 약하면 앞지를 수 없음
    if now_power > 1:
        # 나보다 약한애들 숫자를 셈
        count = segment_sum(1, 1, N, 1, now_power-1)


    update(1, 1, N, now_power, 1)
    print(i+1-count)



