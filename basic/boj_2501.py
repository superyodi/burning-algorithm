N, K = map(int, input().split())

cnt = 1;
p = N;
q = 1
flag = True

while q < p+1:

    if p % q:
        q += 1

    else:
        if cnt == K:
            print(q)
            flag = False
            break
        q += 1
        cnt += 1

if flag:
    print(0)