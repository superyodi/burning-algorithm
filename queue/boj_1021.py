# 회전하는 큐

import sys, collections

N, M = map(int, sys.stdin.readline().split(' '))
ele = list(map(int, map(int, sys.stdin.readline().split(' ')) ))

r_q = collections.deque([i+1 for i in range(N)])
answer = 0

for el in ele:
    if r_q[0] == el:
        r_q.popleft()

        continue

    step = 0

    while True:
      step += 1
      size = len(r_q)

      # print(r_q, el, step)
      if r_q[step] == el:

          for _ in range(step):
              tmp = r_q.popleft()
              r_q.append(tmp)
          r_q.popleft()
          answer += step
          break

      if r_q[size-step] == el:
          for _ in range(step-1):
              tmp = r_q.pop()
              r_q.appendleft(tmp)
          r_q.pop()
          answer += step
          break


print(answer)