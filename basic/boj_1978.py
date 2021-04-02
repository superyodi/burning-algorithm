def find_decimal(n):
    if n == 1:
        return False

    div_n = n - 1

    while div_n > 1:
        if n % div_n == 0:
            return False
        div_n -= 1

    return True


N = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(N):
    if find_decimal(arr[i]):
        cnt += 1

print(cnt)