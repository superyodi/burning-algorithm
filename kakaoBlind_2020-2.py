def solution(new_id):
    new_id = new_id.lower()
    # 1. 대 -> 소
    print("afrer 1_id: {}".format(new_id))

    # 2. 영어, 숫자, _ , -, . 아니면 제거
    del_list = list("~!@#$%^&*()=+[{]}:?,<>")
    for i in range(len(new_id)):
        if new_id[i] in del_list:
            new_id = new_id.replace(new_id[i], 'X')

    new_id = new_id.replace('X', '')

    # 3. .. 연속 -> . 치환
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    # 4. . 가 처음 || 끝 -> 제거
    if new_id:
        tmp_id = new_id
        if tmp_id[0] == '.': new_id = new_id[1:]
        if tmp_id[-1] == '.': new_id = new_id[:-1]

    # 5. 빈 문자열 -> a
    if not new_id: new_id = 'a'

    # 6. len > 15 -> new_id[0:15]
    if len(new_id) > 15:
        new_id = new_id[0:15]
    # 6-1. if new_id[-1] == '.' -> 제거
    if new_id[-1] == '.':
        new_id = new_id[:-1]

    # 7.
    if len(new_id) < 3: new_id += new_id[-1] * (3 - len(new_id))

    return new_id


def solution3(info, query):
    answer = []
    people = []
    # info를 항목별로 split
    for person in info:
        people.append(person.split())

    # query 재가공
    q_list = []
    for q in query:
        q_list.append((q.replace("and", "").split()))

    for q in q_list:
        q_dict = dict()
        score = q[-1]

        for idx, val in enumerate(q):
            if val != '-' and idx != len(q) - 1:
                q_dict[idx] = val

        count = 0
        for person in people:

            if person[-1] < score:
                continue

            # check the conditions

            else:
                if not q_dict:
                    count += 1
                    continue

                for key in q_dict.keys():
                    # print(key)
                    if person[key] != q_dict[key]: break

                else:
                    count += 1
                print(q_dict, count)

        answer.append(count)

    print("사람:", people)
    print("쿼리:", q_list)
    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print()
solution3(info, query)



