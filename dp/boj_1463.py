# x값 입력받음
x = int(input())

# dp_x 배열 생성
# dp_x[x] = cal_count
dp_x = [0 for _ in range(x+1)]

# dp_x[x] = dp_x[x-1] + 어떤 최적의 연산
# dp_x[x-1] 도 역시 이전의 연산 + 최적의 연산..
dp_x[1] = 0

# i가 1부터 x까지
for i in range(2, x+1):
    # 아니면 i - 1
    dp_x[i] = dp_x[i-1] + 1
    # i가 3으로 나눠짐
    if not i%3 and dp_x[i] > dp_x[i//3]:
        dp_x[i] = dp_x[i//3] + 1
    # i가 2로 나눠짐
    if not i%2 and dp_x[i] > dp_x[i//2]:
        dp_x[i] = dp_x[i//2] + 1

print(dp_x[x])