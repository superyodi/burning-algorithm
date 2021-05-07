# [호텔 방배정]




# 시간초과
# 정확성: 78.8
# 효율성: 0.0
# 합계: 78.8 / 100.0

def solution(k, room_number):
    answer = []
    room = [False for i in range(k + 1)]

    for num in room_number:
        if not room[num]:
            room[num] = True
            answer.append(num)
            continue

        _num = num
        while room[_num]:
            _num += 1

        room[_num] = True
        answer.append(_num)

    return answer

# 채점 결과
# 정확성: 78.8
# 효율성: 3.0
# 합계: 81.8 / 100.0

def solution(k, room_number):
    answer = []
    max_num = max(room_number)
    room = [False for i in range(max_num + 1)]
    room_size = 0
    is_full = False

    for num in room_number:

        # 방이 차지 않았을때
        if not is_full:

            if not room[num]:

                room[num] = True
                answer.append(num)
                room_size += 1

            else:

                _num = num
                while _num < len(room) and room[_num]:
                    _num += 1

                if _num < len(room):
                    room[_num] = True
                    answer.append(_num)
                    room_size += 1

                else:
                    max_num += 1
                    answer.append(max_num)

            if room_size == len(room) - 1:
                is_full = True

        else:
            max_num += 1
            answer.append(max_num)

    print(room)

    return answer


# 채점 결과
# 정확성: 78.8
# 효율성: 21.2
# 합계: 100.0 / 100.0


def solution(k, room_number):
    answer = []

    max_number = 0
    rooms = dict()

    for num in room_number:

        if num not in rooms:
            answer.append(num)
            rooms[num] = num + 1

        else:

            key = num
            path = []
            while key in rooms:
                path.append(key)
                key = rooms[key]

            while path:
                now = path.pop()
                rooms[now] = key + 1

            rooms[key] = key + 1

            answer.append(key)

    return answer