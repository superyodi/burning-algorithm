# 2019 카카오 개발자 겨울 인턴십 > 튜플

def solution(s):
    result = []
    set_s = set()
    s = s[2:-2]

    s = s.split("},{")

    s_tuple = []
    for _s in s:
        _s = _s.split(",")
        s_tuple.append(_s)

    s_tuple = sorted(s_tuple, key=lambda x: len(x))

    for st in s_tuple:
        for s in st:
            if s not in set_s:
                set_s.add(s)
                result.append(int(s))

    return result
