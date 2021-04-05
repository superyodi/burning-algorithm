# 빗물
# 시뮬레이션

def find_right(arr):
    return arr.index(max(arr))

H, W = map(int, input().split())
block = list(map(int, input().split()))

water = 0
i = 1
left = 0

while i < W:
    if block[left] <= block[i]:
        water += sum(list(map(lambda x : block[left] - x, block[left:i])))
        left = i
    i += 1

while left < W-1:
    right = find_right(block[left+1:]) + left + 1
    water += sum(list(map(lambda x : block[right] - x, block[left+1:right + 1])))
    left = right


print(water)


# 3 5
# 0 0 0 2 0