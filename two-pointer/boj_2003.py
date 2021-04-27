N, M = map(int,input().split(' '))
A = list(map(int,input().split(' ')))

count = 0
left = right = 0
_sum = A[left]

while left < len(A) and right < len(A):

    if _sum < M:
        if right < N -1:
            right += 1
            _sum += A[right]
        else:
            break

    elif _sum == M:
        count += 1
        # print(_sum, left, right)
        _sum -= A[left]
        left += 1

    else:
        _sum -= A[left]
        left += 1

print(count)


