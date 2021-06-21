import re


def solution(s):
    b_count, z_count = 0, 0

    while s != '1':
        s, tmp = re.subn(pattern='0', repl='', string=s)
        z_count += tmp

        s = str(bin(len(s)))[2:]
        b_count += 1

    return [b_count, z_count]