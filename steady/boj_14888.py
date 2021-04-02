# 연산자 끼워넣기
# 순열이용

from itertools import permutations

def cal(opers, num):
    result = num[0]
    for i in range(len(opers)):
        result = operate(opers[i], result, num[i+1])

    return result

def operate(flag, a, b):
    if flag == 0:
        return a+b
    elif flag == 1:
        return a-b
    elif flag ==2:
        return a*b
    elif flag == 3:
        if a <0 and b > 0:
            return -(-a//b)
        return a//b
    else:
        print("잘못입력했습니다")


operator = []
_min = 10**9
_max = -10**9
N = int(input())
A = list(map(int, input().split()))
_input = list(map(int, input().split()))

for i in range (4):
    x = _input[i]
    if x:
        operator += [i] * x


operators = list(set(permutations(operator)))

for oper in operators:
    result = cal(oper, A)

    _min = min(_min, result)
    _max = max(_max, result)

print(_max)
print(_min)

