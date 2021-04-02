N = int(input())

arr = list(map(int, input().split()))
min = 10**6
max = -10**6

for num in arr:
    if num <= min:
        min = num

    if num >= max:
        max = num
print(min,max)

