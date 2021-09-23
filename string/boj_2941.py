# 백준 크로아티아 알파벳

import sys

line = sys.stdin.readline().strip()

i = 0
cnt = 0
while i < len(line):
    if line[i] == 'd':
        if i+1 < len(line) and line[i:i+2] == 'd-':
            cnt += 1
            i += 2
            continue

        if i+2 < len(line) and line[i:i+3] == 'dz=':
            cnt += 1
            i += 3
            continue

    if line[i] == 'c':
        if i+1 < len(line):
            if line[i:i+2] in ['c-', 'c=']:
                cnt += 1
                i += 2
                continue

    if line[i] == 'l' and i+1 < len(line) and line[i:i+2] == 'lj':
        cnt += 1
        i += 2
        continue

    if line[i] == 'n' and i+1 < len(line) and line[i:i+2] == 'nj':
        cnt += 1
        i += 2
        continue

    if line[i] == 's' and i+1 < len(line) and line[i:i+2] == 's=':
        cnt += 1
        i += 2
        continue

    if line[i] == 'z' and i+1 < len(line) and line[i:i+2] == 'z=':
        cnt += 1
        i += 2
        continue

    cnt += 1
    i += 1

print(cnt)