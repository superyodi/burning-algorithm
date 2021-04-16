import collections


def solution(s):
    def check(str):
        stack = []

        for ch in str:
            if ch in {"[,(,{"}:
                stack.append(ch)
                continue

            if stack:
                if ch == ']' and stack[-1] == '[':
                    stack.pop()
                    continue

                if ch == ')' and stack[-1] == '(':
                    stack.pop()
                    continue

                if ch == '}' and stack[-1] == '{':
                    stack.pop()
                    continue
            stack.append(ch)

        if stack:
            return False
        return True

    answer = 0

    s = collections.deque(s)

    cnt = len(s)

    # 회전
    while cnt:

        s.append(s.popleft())

        if check(s):
            answer += 1

        cnt -= 1

    return answer