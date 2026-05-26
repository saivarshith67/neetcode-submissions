class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j) -> int:
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return 0

            if grid[i][j] == 0:
                return 0

            grid[i][j] = 0

            return (
                1 + 
                dfs(i + 1, j) +
                dfs(i - 1, j) +
                dfs(i, j + 1) +
                dfs(i, j - 1)
            )

        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    max_area = max(max_area, area)

        return max_area


        