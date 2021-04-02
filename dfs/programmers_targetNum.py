def solution(n):
    answer = []
    n_operator = []
    final_num = []

    s_num = str(n)

    if len(s_num) == 1: return [0, n]

    l_num = ""
    r_num = ""
    while len(s_num) > 1:
        # 가운데값 0일때 처리를 해줘야하는데;....
        mid = len(s_num) // 2

        if mid % 2 == 0:
            l_num = s_num[:mid]
            s_num = l_num[mid:]
        else:
            if s_num[0] < s_num[mid]:
                l_num = s_num[:mid+1]
                r_num = s_num[mid+1:]
            else:
                l_num = s_num[:mid]
                r_num = s_num[mid:]

        str_num = str(int(l_num) + int(r_num))
        print(str_num)


    # 1. mid를 기준으로 cut
    # id str_n[0] --> mid 이동 더이상 0이 아닐때까지 그리고 cut
    # if mid가 홀수라면
    # -> str_n[0] 과 str_n[mid] 숫자 비교

    # cut -> sum -> cut 반복

    print(n)

    return answer

# def dfs():