from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROTTEN = 2
        FRESH = 1

        rows, cols = len(grid), len(grid[0])

        fresh_cnt = 0
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == FRESH:
                    fresh_cnt += 1
                elif grid[i][j] == ROTTEN:
                    q.append((i, j))

        minutes = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q and fresh_cnt > 0:
            size = len(q)

            for _ in range(size):
                x, y = q.popleft()

                for dx, dy in directions:
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < rows and 0 <= yy < cols and grid[xx][yy] == FRESH:
                        grid[xx][yy] = ROTTEN
                        fresh_cnt -= 1
                        q.append((xx, yy))

            minutes += 1

        return minutes if fresh_cnt == 0 else -1