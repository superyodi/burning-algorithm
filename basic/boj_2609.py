
def cal(n,m):
    gcd = min(n,m)


    while gcd:

        if n % gcd == 0 and m % gcd == 0:
            break

        gcd -= 1

    lcm = n//gcd * m//gcd * gcd

    print(gcd)
    print(lcm)

    return






N, M = map(int, input().split())
cal(N, M)

