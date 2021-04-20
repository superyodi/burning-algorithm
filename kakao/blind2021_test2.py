# https://programmers.co.kr/learn/courses/30/lessons/72411
# 2021 KAKAO BLIND RECRUITMENT > 메뉴 리뉴얼

import itertools

def solution(orders, course):
    answer = []
    # 조합이라니...
    # n_C_r
    dic_course = dict()
    while course:
        r = course.pop(0)

        for order in orders:
            if len(order) >= r:
                for _course in list(itertools.combinations(order, r)):
                    _course = tuple(sorted(list(_course)))
                    if _course not in dic_course:
                        dic_course[_course] = 1

                    else:
                        dic_course[_course] += 1

    dic_course = sorted(dic_course.items(), key=lambda x: (len(x[0]), -x[1]))
    # print(dic_course)

    now_len = len(dic_course[0][0])
    max_cnt = dic_course[0][1]

    for key, val in dic_course:
        if val == 1: continue
        if len(key) > now_len:
            max_cnt = val
            now_len = len(key)
            answer.append("".join(sorted(list(key))))

        elif len(key) == now_len:
            if max_cnt == val:
                answer.append("".join(sorted(list(key))))

    answer = sorted(answer)

    return answer


# 문제 풀이 과정 : https://velog.io/@superyodi/2021-KAKAO-BLIND-%EB%A9%94%EB%89%B4-%EB%A6%AC%EB%89%B4%EC%96%BC