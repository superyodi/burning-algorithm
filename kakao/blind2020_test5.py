arr = []


def solution(n, build_frame):
    global arr
    arr = [[[False, False] for _ in range(n + 1)] for _ in range(n + 1)]

    # print(*arr, sep='\n')
    for cmd in build_frame:
        x, y, a, b = cmd
        if b == 1:
            if build(x, y, a, n):
                arr[y][x][a] = True
        else:
            delete(x, y, a, n)

    answer = check(n)
    return answer


def build(x, y, a, n):
    if a == 0:  # 기둥
        if y == 0 or (x - 1 >= 0 and arr[y][x - 1][1]) or arr[y][x][1] or (y - 1 >= 0 and arr[y - 1][x][0]):
            return True


    else:  # 보
        if (y - 1 >= 0 and arr[y - 1][x][0]) or (y - 1 >= 0 and x + 1 < n + 1 and arr[y - 1][x + 1][0]) or \
                (x - 1 >= 0 and x + 1 < n + 1 and arr[y][x - 1][1] and arr[y][x + 1][1]):
            return True

    return False


def delete(x, y, a, n):
    arr[y][x][a] = False
    if a == 0:  # 기둥
        # 윗 기둥
        if y + 1 < n + 1 and arr[y + 1][x][0] and not build(x, y + 1, 0, n):
            arr[y][x][0] = True
            return
        # 왼쪽 위 보
        if x - 1 >= 0 and y + 1 < n + 1 and arr[y + 1][x - 1][1] and not build(x - 1, y + 1, 1, n):
            arr[y][x][0] = True
            return

        # 오른쪽 위 보
        if y + 1 < n + 1 and arr[y + 1][x][1] and not build(x, y + 1, 1, n):
            arr[y][x][0] = True
            return



    else:  # 보
        # 왼쪽 보
        if x - 1 >= 0 and arr[y][x - 1][1] and not build(x - 1, y, 1, n):
            arr[y][x][1] = True
            return
        # 오른쪽 보
        if x + 1 < n + 1 and arr[y][x + 1][1] and not build(x + 1, y, 1, n):
            arr[y][x][1] = True
            return
        # 왼쪽  위 기둥
        if arr[y][x][0] and not build(x, y, 0, n):
            arr[y][x][1] = True
            return
        # 오른쪽 위 기둥
        if x + 1 < n + 1 and arr[y][x + 1][0] and not build(x + 1, y, 0, n):
            arr[y][x][1] = True
            return

    # print(x, y, a, "삭제 결과: ", not arr[y][x][a])


def check(n):
    answer = []
    for x in range(n + 1):
        for y in range(n + 1):
            if arr[y][x][0]:
                answer.append([x, y, 0])
            if arr[y][x][1]:
                answer.append([x, y, 1])

    return answer
