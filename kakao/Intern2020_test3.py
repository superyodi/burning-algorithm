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

