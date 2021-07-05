# 백준 - 고스택

import sys

cmd_list = []
stack = []
answer = []

def calculate(input):
    # print(input)
    global stack

    if input[0:3] == "NUM":
        num = int(input.split(" ")[1])
        stack.append(num)
        return True

    elif input[0:3] == "POP":
        if stack:
            stack.pop()
            return True
        return False

    elif input[0:3] == "INV":
        if stack:
            num = stack.pop()
            stack.append(-num)
            return True
        return False

    elif input[0:3] == "DUP":
        if stack:
            num = stack[-1]
            stack.append(num)
            return True
        return False

    elif input[0:3] == "SWP":
        if len(stack) > 1:
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1)
            stack.append(num2)
            return True
        return False

    elif input[0:3] == "ADD":
        if len(stack) > 1:
            num1 = stack.pop()
            num2 = stack.pop()
            result = num1 + num2
            if check(result):
                stack.append(result)
                return True
        return False

    elif input[0:3] == "SUB":
        if len(stack) > 1:
            num1 = stack.pop()
            num2 = stack.pop()
            result = num2 - num1
            if check(result):
                stack.append(result)
                return True
        return False

    elif input[0:3] == "MUL":
        if len(stack) > 1:
            num1 = stack.pop()
            num2 = stack.pop()
            result = num1 * num2
            if check(result):
                stack.append(result)
                return True
        return False

    elif input[0:3] == "DIV":
        if len(stack) > 1:
            num1 = stack.pop()
            num2 = stack.pop()

            if num1 == 0:
                return False
            result = abs(num2) // abs(num1)
            # 음수가 하나라도 있을때
            if num1 < 0 or num2 < 0:
                if not (num1 < 0 and num2 < 0):
                    result *= -1

            stack.append(result)
            return True
        return False

    elif input[0:3] == "MOD":
        if len(stack) > 1:
            num1 = stack.pop()
            num2 = stack.pop()  # 피제수

            if num1 == 0:
                return False

            result = abs(num2) % abs(num1)
            # 음수가 하나라도 있을때
            if num2 < 0:
                result *= -1
            stack.append(result)
            return True
        return False

    return False


def check(num):
    MAX_NUM = 10 ** 9
    if abs(num) > MAX_NUM:
        return False
    return True


while True:

    input = sys.stdin.readline()
    if input == '\n':
        cmd_list.clear()
        continue

    input = input.strip()



    if input == "QUIT":
        for str in answer:
            print(str)

        sys.exit(0)


    elif input == "END":
        N = int(sys.stdin.readline())
        for _ in range(N):
            num = int(sys.stdin.readline())
            stack = [num]

            for cmd in cmd_list:
                result = calculate(cmd)
                if not result:
                    answer.append("ERROR")
                    break

            else:
                if len(stack) == 1:
                    answer.append(stack[-1])

                else:
                    answer.append("ERROR")

        answer.append(" ")
        continue
    else:
        cmd_list.append(input)

