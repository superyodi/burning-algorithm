# 불량 사용자


import itertools


def solution(user_id, banned_id):
    answer = 0

    # idx : alpha
    idx_list = []

    for b_id in banned_id:
        b_id = list(b_id)

        tmp_d = {i: b_id[i] for i in range(len(b_id))}

        idx_list.append(tmp_d)

    result_id = []

    for dic in idx_list:
        ids = []

        for u_id in user_id:
            if len(dic) != len(u_id):
                continue

            for i in range(len(u_id)):
                if u_id[i] != dic[i] and dic[i] != '*':
                    break
            else:

                ids.append(u_id)
        result_id.append(ids)

    product = list(itertools.product(*result_id))

    result_ids = set()
    size = len(banned_id)

    for _list in product:
        s_list = set(_list)
        if len(s_list) == size:
            result_ids.add(tuple(sorted(s_list)))

    return len(result_ids)