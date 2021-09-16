visited = []
result = set()

def solution(numbers):
    global visited, result

    visited = [False for _ in range(len(numbers))]

    # 중복 안됨
    dfs(numbers, "")
    answer = len(result)

    return answer


def dfs(numbers, now):
    # print("dfs: ", now)
    if now != "":
        num = int(now)
        if is_prime(num) and num not in result:
            result.add(num)

    if len(now) == len(numbers):
        return

    for i in range(len(numbers)):
        if not visited[i]:
            visited[i] = True
            dfs(numbers, now + numbers[i])
            visited[i] = False


def is_prime(n):
    if n == 1 or n == 0: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1

    return True