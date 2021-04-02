from collections import deque

def cal_bin(N):
    bin_N = deque()

    # 1. search MSB
    msb = 0

    while True:
        if N < 1<<msb:
            bin_N.appendleft(str(msb-1))
            N -= 1<<msb-1
            break

        msb += 1

    # 2.search LSB
    lsb = msb - 1
    while lsb >= 0:
        if N >= 1<<lsb:
            bin_N.appendleft(str(lsb))
            N -= 1<<lsb

        lsb -= 1

    return list(bin_N)


T = int(input())

t = 0

while t < T:
    N = int(input())
    arr = cal_bin(N)
    print(' '.join(arr))

    t+=1
