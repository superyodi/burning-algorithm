# 백준 퇴사

import sys, collections


N = int(sys.stdin.readline())

plans = [0]


def bfs(plans):
    max_sum = 0
    queue = collections.deque()
    # day, now_sum
    inform = (0, 0)

    queue.append(inform)

    while queue:
        day, now_sum = queue.popleft()

        max_sum = max(max_sum, now_sum)


        if day+1 <= N:
            queue.append((day + 1, now_sum))
            if day + plans[day + 1][0] <= N:
                queue.append((day + plans[day + 1][0], now_sum + plans[day + 1][1]))


    return max_sum




for _ in range(N):
     plans.append(list(map(int, sys.stdin.readline().split(' '))))

print(bfs(plans))




