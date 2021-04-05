# 비슷한 문제: https://www.acmicpc.net/problem/17144

from collections import deque
square = []

# 실제 입력값보다 -1해서 넣어줌
def rotate(y1, x1, y2, x2):
    changes = []
    tmps = deque()

    # 좌-우
    for x in range(x1, x2):
        tmp = square[y1][x+1]
        if tmps:
            square[y1][x+1] = tmps.popleft()
        else:
            square[y1][x+1] = square[y1][x]

        tmps.append(tmp)
        changes.append(square[y1][x+1])

    # 위-아래
    for y in range(y1, y2):
        tmp = square[y + 1][x2]
        square[y + 1][x2] = tmps.popleft()
        tmps.append(tmp)
        changes.append(square[y + 1][x2])

    # 우-좌
    for x in range(x2, x1, -1):
        tmp = square[y2][x-1]
        square[y2][x - 1] = tmps.popleft()
        tmps.append(tmp)
        changes.append(square[y2][x-1])

    # 아래-위
    for y in range(y2, y1, -1):
        tmp = square[y-1][x1]
        square[y - 1][x1] = tmps.popleft()
        tmps.append(tmp)
        changes.append(square[y - 1][x1])

    return min(changes)


def solution(rows, columns, queries):
    answer = []
    global square
    square = [[0] * columns for _ in range(rows)]
    num = 1

    # 배열 초기화
    for r in range(rows):
        for c in range(columns):
            square[r][c] = num
            num += 1

    for query in queries:
        y1, x1, y2, x2 = query
        answer.append(rotate(y1 - 1, x1 - 1, y2 - 1, x2 - 1))

    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100,97,[[1,1,100,97]]))


# 실제 테스트에선 시간초과 이슈가 있었다
# 이동 전 좌표값을 저장하기 위해 rotate 함수에서 square 배열을 deepcopy하는 방식으로 구현하였다
# 다시 풀어보니 변경 전 값을 queue에 넣어주면 rotate함수를 호출할때마다 배열 W*H 만큼 copy할 필요가 없었다
