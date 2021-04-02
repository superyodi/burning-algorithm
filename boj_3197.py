# https://www.acmicpc.net/problem/3197
# 백조의 호수


# 조건 3. 현재 백조의 위치 파악
# 조건 3-1. 백조가 만날수 있는 지 확인
# ----아래부터 while돌면서 체
# 조건 1. 날이 지나면서 빙판이 녹음
# 조건 2. 백조가 만날 수 있도록 가로, 세로로 길이 트여있어야한다.
# squre[:][]  == 1 || square[][:] == 1

# dfs 방식으로 새의 가동범위 색칠
def check_bird(y, x, my_c, your_c):
    if map[y][x] == 'L':
        # 상
        if y != 0: return check_bird(y - 1, x, my_c, your_c)
        # 하
        if y + 1 < len(map): return check_bird(y + 1, x, my_c, your_c)
        # 좌
        if x != 0: return check_bird(y, x - 1, my_c, your_c)
        # 우
        if x + 1 < len(map[0]): return check_bird(y, x + 1, my_c, your_c)
    elif map[y][x] == '.':
        map[y][x] = my_c
        # 상
        if y != 0: return check_bird(y-1, x, my_c, your_c)
        # 하
        if y+1 < len(map): return check_bird(y+1, x,  my_c, your_c)
        # 좌
        if x != 0: return check_bird(y, x-1,  my_c, your_c)
         # 우
        if x+1 < len(map[0]): return check_bird(y, x+1, my_c, your_c)
    # 다른 백조의 가동범위와 일치할때
    elif map[y][x] == your_c:
        return True

    # 막혀있으면 걍 return
    else: return False

def melting_ice(y, x):
    # 상
    if y != 0: map[y-1][x] = '.'
    # 하
    if y + 1 < len(map): map[y+1][x] = '.'
    # 좌
    if x != 0: map[y][x-1] = '.'
    # 우
    if x + 1 < len(map[0]): map[y][x+1] = '.'


R, C = map(int, input().split())

# print(R, C)

map = []
birds = []
soon_water = []

for i in range(R):
    map.append(list(input()))

pre = [0, 0]
for y in range(R):
    for x in range(C):
        if map[y][x] == 'L':
            birds.append([y, x])



count = 0
is_okay = False

print(check_bird(birds[0][0], birds[0][1], 'B', 'W'))
print(map)
print(check_bird(birds[0][0], birds[0][1], 'B', 'W'))
print(map)



# while not is_okay:
#     # 백조가 만날수있나 확인
#     # bird1의 color는 B, bird2의 color는 W
#     is_okay = check_bird(birds[0][0], birds[0][1], 'B', 'W')
#     if is_okay:
#         break
#     is_okay = check_bird(birds[1][0], birds[1][1], 'W', 'B')
#     if is_okay:
#         break
#
#     # 얼음물은 녹고있오요,,,,ㅎ,,,,
#     for y in range(R):
#         for x in range(C):
#             if map[y][x] == '.':
#                 melting_ice(y, x)
#
#
#     count += 1
#     print(count)



print(count)

'''
3 5
....L
XXX..
L....


'''