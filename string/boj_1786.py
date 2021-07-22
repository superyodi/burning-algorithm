# 백준 - 찾기
# KMP

kmp_count = 0
idxs = []
# pattern에서 lps 찾기
def make_lps(p):
    lps = [0] * len(p)

    pre, now = 0, 1

    while now < len(p):
        if p[now] == p[pre]: # 이전의 char과 지금의 char이 같을때
            pre += 1
            lps[now] = pre
            now += 1

        else:
            if pre != 0: # 이전의 pre가 0이 아닐때
                pre = lps[pre-1]

            else:
                lps[now] = 0
                now += 1

    return lps

def search_kmp(s, p): # string, pattern
    global kmp_count
    N, M = len(s), len(p)

    lps = make_lps(p)
    i, j = 0, 0

    while i < N:
        if p[j] == s[i]:
            j+=1; i+=1
        else:
            if j!= 0:
                # lps[]의 값은 다음에 조사할 인덱스를 정하는 기준
                j = lps[j-1]
            else:
                i += 1

        if j == M:
            kmp_count += 1
            j = lps[j-1]
            idxs.append(str(i-M+1))
            # print("{}번째 패턴 찾음: {}에 위치".format(kmp_count, i-M))



T = input()
P = input()

search_kmp(T, P)

print(kmp_count)
print(" ".join(idxs))