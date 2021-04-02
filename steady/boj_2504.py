bracket = input()
stack = []
flag = True
# 괄호 찾기
for b in bracket:
    if b in {"(", "["}:
        stack.append(b)
    if b == ")":
        # stack top에 숫자가 있으면 숫자가 안 나올때까지 pop, 그리고 더해준다
        if not stack:
            flag = False
            print("0")
            break

        if type(stack[-1]) == int:
            tmp = stack.pop()
            while stack and type(stack[-1]) == int:
                tmp += stack.pop()

            if stack and stack[-1] == "(":
                stack.pop()
                stack.append(tmp * 2)

        if stack and stack[-1] == "(":
            stack.pop()
            stack.append(2)

    if b == "]":
        if not stack:
            flag = False
            print("0")
            break

        if type(stack[-1]) == int:
            tmp = stack.pop()
            while stack and type(stack[-1]) == int:
                tmp += stack.pop()

            if stack and stack[-1] == "[":
                stack.pop()
                stack.append(tmp * 3)

        if stack and stack[-1] == "[":
            stack.pop()
            stack.append(3)

answer = 0
if flag:
    for num in stack:
        if type(num) == int:
            answer += num

        else:
            print("0")
            break
    else:
        print(answer)
