def solution(record):
    answer = []

    # 걍 업데이트가 된다.
    info = dict()
    for line in record:
        line = line.split(' ')

        if line[0] == "Enter":
            answer.append([line[1], "님이 들어왔습니다."])

            info[line[1]] = line[2]


        elif line[0] == "Leave":
            answer.append([line[1], "님이 나갔습니다."])


        else:
            info[line[1]] = line[2]

    for i, line in enumerate(answer):
        line[0] = info[line[0]]

        answer[i] = "".join(line)

    return answer