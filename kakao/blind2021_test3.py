# 순위 검색

# [Try 1]
# 정확성: 40.0
# 효율성: 0.0
# 합계: 40.0 / 100.0


import re


def solution(info, query):
    answer = []
    d_info = dict()
    scores = []

    # info 처리
    for idx, _info in enumerate(info):
        _info = list(_info.split(" "))
        score = int(_info[-1])
        scores.append(score)

        for key in _info[:-1]:
            if key not in d_info:
                d_info[key] = set([idx])

            else:
                d_info[key].add(idx)

    # query 처리
    for _query in query:

        _query = re.sub('and|-', '', _query)
        _query = list(_query.split(" "))
        _query = list(filter(lambda x: x != '', _query))
        score = int(_query.pop())

        count = 0
        if not _query:
            count = len([_ for _ in scores if _ >= score])

        else:
            idx_set = d_info[_query.pop()]

            for q in _query:
                # print(d_info[q])
                idx_set = idx_set.intersection(d_info[q])

            for idx in idx_set:
                if scores[idx] >= score:
                    count += 1

        answer.append(count)

    return answer


# [Try 2]
# 정확성: 40.0
# 효율성: 0.0
# 합계: 40.0 / 100.0

import itertools, collections, re


def solution2(info, query):
    answer = []
    t_info = []
    scores = []

    d_info = collections.defaultdict(set)

    info = list(map(lambda x: x.split(' '), info))

    for idx, _info in enumerate(info):
        data = [
            [_info[0], '-'],
            [_info[1], '-'],
            [_info[2], '-'],
            [_info[3], '-']
        ]

        p_info = list(itertools.product(*data))

        for p in p_info:
            d_info[p].add(idx)

        scores.append(int(_info[-1]))

    for _query in query:

        _query = re.sub('and', '', _query)
        _query = list(_query.split(" "))
        _query = list(filter(lambda x: x != '', _query))
        score = int(_query.pop())

        idxs = d_info[tuple(_query)]

        count = 0

        for idx in idxs:
            if scores[idx] >= score:
                count += 1

        answer.append(count)

    return answer

# 이때 query 시간복잡도 : query 길이 * info 길이 (100000 * 50000)


# [Try 3. Succeed]
# 정확성: 40.0
# 효율성: 60.0
# 합계: 100.0 / 100.0
import itertools, collections, re


def solution3(info, query):
    answer = []
    t_info = []
    d_info = collections.defaultdict(list)

    info = list(map(lambda x: x.split(' '), info))

    for idx, _info in enumerate(info):
        data = [
            [_info[0], '-'],
            [_info[1], '-'],
            [_info[2], '-'],
            [_info[3], '-']
        ]

        p_info = list(itertools.product(*data))

        for p in p_info:
            d_info[p].append(int(_info[-1]))

    for k, v in d_info.items():
        d_info[k] = sorted(v)

    for _query in query:

        _query = re.sub('and', '', _query)
        _query = list(_query.split(" "))
        _query = list(filter(lambda x: x != '', _query))

        target = int(_query.pop())

        scores = d_info[tuple(_query)]

        if not scores:
            answer.append(0)
            continue

        count = 0

        # print("scores", scores, target)

        if scores[-1] < target or not scores:
            answer.append(count)
            continue

        # b-search
        start, end = 0, len(scores)

        while end > start:
            mid = (end + start) // 2

            if scores[mid] < target:
                start = mid + 1

            else:
                end = mid

        answer.append(len(scores) - start)

    return answer



# collections.defaultdict
# itertools.product
# re.sub

# binary search
# lower-bound