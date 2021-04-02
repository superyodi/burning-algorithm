# 가운데를 말해요 https://www.acmicpc.net/problem/1655

# 업데이트 될때마다 가운데 숫자를 계산 그리고 출력
def cal_mid(n_list, start, end, num):
    if start == end: return start
    mid = (start + end) // 2
    if num <= n_list[mid]:
        return cal_mid(n_list, start, mid, num)
    else:
        return cal_mid(n_list, mid+1, end, num)

n = int(input())
num_list = []
mid_list = []

for i in range(n):
    now = int(input())
    idx = cal_mid(num_list, 0, i, now)

    if idx == i: num_list.append(now)
    else: num_list.insert(idx, now)

    n_len = len(num_list)

    # 숫자의 길이가 홀수
    if n_len % 2:
        mid_list.append(num_list[n_len // 2])
    # 숫자의 길이가 짝수
    else:
        mid_list.append(min(num_list[n_len // 2 - 1], num_list[n_len // 2]))

for mid in mid_list:
    print(mid)
