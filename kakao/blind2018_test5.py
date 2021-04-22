import collections

def make_multiset(_str):
    _str = _str.lower()

    multi_set = []
    skip_idx = -1

    for i in range(len(_str) - 1):
        if not _str[i].isalpha() or i == skip_idx:
            continue
        if not _str[i + 1].isalpha():
            skip_idx = i + 1
            continue
        multi_set.append(_str[i:i + 2])

    return multi_set


def make_similiarity(set1, set2):
    counter1 = collections.Counter(set1)
    counter2 = collections.Counter(set2)

    intersection = counter1 & counter2
    union = counter1 | counter2

    similiarity = int(sum(intersection.values()) / sum(union.values()) * 65536)

    return similiarity


def solution(str1, str2):
    answer = 0

    set1 = make_multiset(str1)
    set2 = make_multiset(str2)

    if len(set1) == 0 and len(set2) == 0:
        return 65536

    return make_similiarity(set1, set2)

