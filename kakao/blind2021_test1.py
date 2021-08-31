# 카카오 - 신규아이디 추천 (정규식 문제)


# [try 1. 정규식 안쓴 풀이]

'''

def solution(new_id):
    answer = ''


    # case 1
    new_id = new_id.lower()

    # case 2
    x_str = list("~!@#$%^&*()=+[{]}:?,<>/")
    for ch in new_id:
        if ch in x_str:
            new_id = new_id.replace(ch, "")

    # case 3
    while True:
        if ".." in new_id:
            new_id = new_id.replace("..", ".")
        else:
            break

    # case 4
    new_id = list(new_id)

    if new_id:
        if new_id[0] == '.':
            new_id.pop(0)

        elif new_id[-1] == '.':
            new_id.pop()

    if not new_id:
        new_id = ['a']

    # case 6
    if len(new_id) > 15:
        new_id = new_id[:15]

    # case 7
    if new_id and new_id[-1] == ".":
        new_id.pop()

    # case 8
    while new_id and len(new_id) < 3:
        new_id.append(new_id[-1])


    answer = ''.join(new_id)

    return answer
'''

## # [try 2. 정규식으로 푼 풀이]

import re


def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    new_id = re.sub(r"[^a-z0-9-_.]", '', new_id)
    new_id = re.sub("[..]+", '.', new_id)
    # print(new_id)
    new_id = re.sub("^[.]", '', new_id)
    # print(new_id)
    new_id = re.sub("[.]$", '', new_id)
    # print(new_id)

    if len(new_id) == 0:
        new_id = "a"
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    if len(new_id) <= 2:
        x = new_id[-1]
        new_id = new_id + x * (3 - len(new_id))
    return new_id

