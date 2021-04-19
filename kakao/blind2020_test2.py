# 2020 KAKAO BLIND RECRUITMENT > 괄호 변환

# https://programmers.co.kr/learn/courses/30/lessons/60058

def reverse(u):
    u = list(u)

    for i, v in enumerate(u):
        if v == ")":
            u[i] = "("
        else:
            u[i] = ")"
    return "".join(u)


def check(u):
    stack = []

    for _u in u:
        if _u == ")" and stack:
            if stack[-1] == "(":
                stack.pop()
        else:
            stack.append(_u)

    if stack:
        return False
    return True


def partition(w):
    if w == "":
        return w

    flag = 0
    idx = -1

    # partition
    for i, v in enumerate(w):
        if v == "(":
            flag -= 1
        else:
            flag += 1

        if flag == 0:
            idx = i
            break

    u, v = w[:idx + 1], w[idx + 1:]

    if check(u):

        u += partition(v)
        return u

    else:
        return "(" + partition(v) + ")" + reverse(u[1:-1])


def solution(p):
    if p == "":
        return p

    if check(p):
        return p

    answer = partition(p)
    return answer


# 문제를 이해하기까지 오래 걸렸다.
# 그냥 뇌를 빼놓고 문제에서 하라는대로 하면 되는, 알고리즘적으로는 간단한, 문제였다

# <진행과정>
# 1. partition 함수를 구현하는 부분에서 u와 v를 어떻게 나눠야하는지 고민하다가 일단 (와 )의 갯수가 딱 맞는 그 지점을 u, 그 뒤는 v로 하기로 했다.
# 2. ' 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.' 이 부분에서 생각없이 [::-1] 이렇게 문자열을 뒤집었는데
# 정확도 53%에 당황해서 살펴보니 reverse()를 만들어서 (는 )로, )는 (로 바꿔줘야했다.

