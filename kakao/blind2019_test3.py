import itertools

def solution(relation):
    answer = 0
    # 후보키 조합들
    c_keys = []

    n = len(relation[0])
    colms = list(range(n))
    k = 1

    while k <= n:
        nCr = list(itertools.combinations(colms, k))

        while nCr:
            idxs = list(nCr.pop())
            flag = False

            for key in c_keys:
                cnt = 0
                for idx in key:
                    if idx in idxs:
                        cnt += 1
                if cnt == len(key):
                    flag = True
                    break

            if flag:
                continue

            tmp_set = set()

            for row in range(len(relation)):
                tmp_str = ""
                for idx in idxs:
                    tmp_str += relation[row][idx]

                tmp_set.add(tmp_str)

            # 후보키 여부 판별
            if len(tmp_set) == len(relation):
                answer += 1
                c_keys.append(idxs)

                if k == 1:
                    colms.remove(idxs[0])
                    n -= 1

        k += 1


    return answer

