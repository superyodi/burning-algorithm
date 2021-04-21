# https://programmers.co.kr/learn/courses/30/lessons/67257
# 2020 카카오 인턴십 > 수식 최대화


# [Try 1: Fail]
def solution(expression):
    numbers = []
    operands = {}

    n_idx = 0;
    o_idx = 0

    for idx in range(len(expression)):
        if expression[idx] in {'*', '-', '+'}:
            numbers.append(int(expression[n_idx:idx]))
            n_idx = idx + 1
            if expression[idx] in operands:
                operands[expression[idx]] += 1
            else:
                operands[expression[idx]] = 1

    print(numbers)
    print(operands)

    answer = 0
    return answer

# [Try 2: succeed]
# 1시간 10분

import re, itertools

def calculate(expression, operand):
    # 걍 append해서 리스트 만든거 return
    # 해당 연산자 나올때마다 앞숫자, 연산자, 뒤숫자 빼고
    # 연산 결과 append

    operation = []
    skip_idx = -1

    for idx in range(len(expression)):
        # print("cal: ", operand, operation)
        if idx == skip_idx: continue

        if expression[idx] == operand:
            left = operation.pop()
            right = expression[idx + 1]
            skip_idx = idx + 1

            if operand == "-":
                operation.append(left - right)
            elif operand == "+":
                operation.append(left + right)
            else:
                operation.append(left * right)
        else:
            operation.append(expression[idx])
    return operation


def solution(expression):
    answer = 0

    _expression = list(map(int, re.split('[*+-]', expression)))

    # 문자열 처리
    idx = 1
    operands = set()
    for ch in expression:
        if ch in {'+', '-', '*'}:
            if ch not in operands:
                operands.add(ch)
            _expression.insert(idx, ch)
            idx += 2

    # 연산자 조합(순열) 구하기
    operand_orders = list(itertools.permutations(operands, len(operands)))

    while operand_orders:
        operand_order = operand_orders.pop()
        operation = _expression[:]

        for operand in operand_order:
            operation = calculate(operation, operand)

        operation = abs(operation[-1])
        answer = max(answer, operation)

    return answer

