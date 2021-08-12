import itertools


def solution(clothes):
    dic = {}
    type_list = []
    # dictionary 저장
    for line in clothes:
        name, c_type = line
        if c_type in dic:
            dic[c_type] += 1
        else:
            dic[c_type] = 1
            type_list.append(c_type)

    # combination
    type_size = len(type_list)
    answer = 1

    for key, val in dic.items():
        answer *= (val + 1)

    return answer - 1