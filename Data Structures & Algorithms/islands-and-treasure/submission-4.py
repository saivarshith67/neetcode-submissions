from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        LAND = 2147483647
        TREASURE = 0
        WATER = -1

        rows = len(grid)
        cols = len(grid[0])

        q = deque()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == TREASURE:
                    q.append((i, j))

        while q:
            x,y = q.popleft()

            for dx,dy in directions:
                xx, yy = x + dx, y + dy
                if 0 <= xx < rows and 0 <= yy < cols and grid[xx][yy] == LAND:
                    grid[xx][yy] = grid[x][y] + 1
                    q.append((xx, yy))



