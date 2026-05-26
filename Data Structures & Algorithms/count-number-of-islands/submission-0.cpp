class Solution {
public:
    void dfs(const vector<vector<char>>& grid, vector<vector<bool>>& visited, int i, int j) {
        int m = grid.size();
        int n = grid[0].size();

        // Boundary and validity checks
        if (i < 0 || i >= m || j < 0 || j >= n) return;
        if (grid[i][j] == '0' || visited[i][j]) return;

        visited[i][j] = true;

        // Explore all 4 directions
        dfs(grid, visited, i + 1, j); // down
        dfs(grid, visited, i - 1, j); // up
        dfs(grid, visited, i, j + 1); // right
        dfs(grid, visited, i, j - 1); // left
    }

    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty()) return 0;

        int m = grid.size();
        int n = grid[0].size();
        int count = 0;

        vector<vector<bool>> visited(m, vector<bool>(n, false));

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                // If it's land and not visited
                if (grid[i][j] == '1' && !visited[i][j]) {
                    dfs(grid, visited, i, j);
                    count++;
                }
            }
        }

        return count;
    }
};
