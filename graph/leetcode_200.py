# 200. Number of Islands

# [Try 1. Wrong Answer]
class Solution:
    def __init__(self):
        self.grid = None
        self.visited = None

    def find(self, _y, _x):
        stack = [(_y, _x)]
        # 상,하,좌,우

        while stack:
            y, x = stack.pop()
            self.visited[y][x] = True

            # 상
            if y - 1 >= 0:
                if not self.visited[y - 1][x] and self.grid[y - 1][x] == "1":
                    stack.append((y - 1, x))

            # 하
            if y + 1 < len(self.grid) and self.grid[y + 1][x] == "1":
                if not self.visited[y + 1][x]:
                    stack.append((y + 1, x))

            # 좌
            if x - 1 >= 0 and self.grid[y][x - 1] == "1":
                if not self.visited[y][x - 1]:
                    stack.append((y, x - 1))

            # 우
            if x + 1 < len(self.grid[0]) and self.grid[y][x + 1] == "1":
                if not self.visited[y][x + 1]:
                    stack.append((y, x + 1))

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        cnt = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if self.visited[y][x] or self.grid[y][x] == "0":
                    continue

                self.find(y, x)
                cnt += 1

        return cnt


'''
grid 전체를 다 돌면서 
grid[y][x]의 [y][x+1], [y+1][x] 의 값을 재귀로 찾도록 했다.
하지만 반례가 있었다. 
[[1,1,1],
 [0,1,0],
 [1,1,1]] 이 상황에서 결과는 1인데 2가 나온다. grid[2][0]을 방문하지 않기때문이다
 
'''

# [Try 2. Accepted]	140 ms	15.3 MB
class Solution2:
    def __init__(self):
        self.grid = None
        self.visited = None

    def find(self, _y, _x):
        stack = [(_y, _x)]
        # 상,하,좌,우

        while stack:
            y, x = stack.pop()
            self.visited[y][x] = True

            # 상
            if y - 1 >= 0:
                if not self.visited[y - 1][x] and self.grid[y - 1][x] == "1":
                    stack.append((y - 1, x))

            # 하
            if y + 1 < len(self.grid) and self.grid[y + 1][x] == "1":
                if not self.visited[y + 1][x]:
                    stack.append((y + 1, x))

            # 좌
            if x - 1 >= 0 and self.grid[y][x - 1] == "1":
                if not self.visited[y][x - 1]:
                    stack.append((y, x - 1))

            # 우
            if x + 1 < len(self.grid[0]) and self.grid[y][x + 1] == "1":
                if not self.visited[y][x + 1]:
                    stack.append((y, x + 1))

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        cnt = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if self.visited[y][x] or self.grid[y][x] == "0":
                    continue

                self.find(y, x)
                cnt += 1

        return cnt


'''
grid가 그래프라는 깨닫고 DFS를 iteration 방식으로 구현했다. 
'''
# [Try3. Accepted]	140 ms	15.6 MB

class Solution3:
    def numIslands(self, grid: List[List[str]]) -> int:

        # vistited를 따로 만들필요는 없다.
        # grid[y][x]가 1인것만 방문하면됨
        # 공간 효율 good

        def dfs(_y, _x):
            if _x < 0 or _x >= len(grid[0]) or \
                    _y < 0 or _y >= len(grid) or \
                    grid[_y][_x] == "0":
                return

            grid[_y][_x] = "0"

            # 상,하,좌,우 호출
            dfs(_y, _x - 1);
            dfs(_y, _x + 1)
            dfs(_y + 1, _x);
            dfs(_y - 1, _x)

        count = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):

                if grid[y][x] == "1":
                    dfs(y, x)
                    count += 1

        return count


'''
Solution2에서 iteration 방식으로 구현한걸 recursive하게 바꿨다.
코드 가독성이 좋고 깔끔해졌지만 runtime은 조금 떨어진다. 
성능 측면에선 iteration이 recursive보다 더 좋기때문이다. 
'''