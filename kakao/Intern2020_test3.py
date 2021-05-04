# 보석쇼핑


def solution(gems):
    answer = []
    ends = []
    short_len = 100000

    s_gems = set(gems)

    # 1) end_list 찾기
    # n 돌면서 now == _gems --> end

    end = 0
    while end < len(gems):
        nows = set()
        while nows != s_gems and end < len(gems):
            nows.add(gems[end])

            if nows == s_gems:
                ends.append(end)
                break
            end += 1
        if end == 0:
            return [1, 1]
        end += 1

    # 최소 거리 찾기
    for idx, end in enumerate(ends):
        if idx == 0:
            start = 0
        else:
            start = ends[idx - 1] + 1

        now = end
        while start < now:
            if gems[start] == gems[now]:
                start += 1
                now = end

            else:
                now -= 1

        # print(start, end)

        if end - start < short_len:
            short_len = end - start
            answer = [start + 1, end + 1]

    return answer


# [Try2. Product]
import collections, itertools


def solution(gems):
    answer = []
    ends = []

    d_gems = collections.defaultdict(list)

    for idx, gem in enumerate(gems):
        d_gems[gem].append(idx)

    # print(d_gems)

    idxs = d_gems.values()

    # print(idxs)

    product = list(itertools.product(*idxs))
    print(product)

    short_len = len(gems)

    for p in product:
        start, end = min(p), max(p)

        if end - start < short_len:
            # print(p)
            answer = [start + 1, end + 1]
            short_len = end - start

    return answer


import collections, itertools


def solution(gems):
    answer = []
    ends = []

    d_gems = collections.defaultdict(int)
    _gems = set(gems)

    for idx, gem in enumerate(gems):
        d_gems[gem] += 1

    start = end = 0
    min_len = 100000

    while start <= end and end < len(gems):
        _now = set(gems[start:end + 1])
        # print(_now)
        if _now == _gems:

            if end - start + 1 < min_len:
                min_len = end - start + 1
                answer = [start + 1, end + 1]
            start += 1
        else:
            end += 1

    # print(d_gems)

    return answer


'''
채점 결과
정확성: 33.3
효율성: 57.8
합계: 91.1 / 100.0

'''
import collections


def solution(gems):
    answer = []

    d_gems = collections.defaultdict(int)
    _gems = set(gems)

    for idx, gem in enumerate(gems):
        d_gems[gem] += 1

    start = end = 0
    min_len = 100000

    d_now = collections.defaultdict(int)
    d_now[gems[start]] = 1
    s_now = set()
    s_now.add(gems[start])

    while start <= end and end < len(gems):
        # print(s_now)
        if s_now == _gems:

            if end - start + 1 < min_len:
                min_len = end - start + 1
                answer = [start + 1, end + 1]

            d_now[gems[start]] -= 1

            if d_now[gems[start]] == 0:
                s_now.remove(gems[start])

            start += 1


        else:
            end += 1
            if end < len(gems):
                d_now[gems[end]] += 1
                s_now.add(gems[end])

    return answer


# 통과
def solution(gems):
    if list(set(gems)) == gems:
        return [1, len(gems)]

    if len(set(gems)) == 1:
        return [1, 1]

    start = end = 0
    answer = [0, len(gems)]

    d_gems = {gems[start]: 1}
    g_size = len(set(gems))

    while start < len(gems) and end < len(gems):

        # 물건종류 다 가지고 있을때, s를 줄여나가면서 최소길이 찾음

        if len(d_gems) == g_size:

            if end - start < answer[1] - answer[0]:
                answer = [start + 1, end + 1]

            d_gems[gems[start]] -= 1

            if d_gems[gems[start]] == 0:
                del (d_gems[gems[start]])

            start += 1

        else:
            end += 1
            if end < len(gems):
                if gems[end] not in d_gems:
                    d_gems[gems[end]] = 1

                else:
                    d_gems[gems[end]] += 1

    return answer