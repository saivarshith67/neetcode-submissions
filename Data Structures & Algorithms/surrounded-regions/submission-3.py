class Solution:
    """
    IDEA:
    iterate through the borders if you find any o perform dfs, mark it's
    component as T as we are for sure that they are not surrounded by X

    then iterate through entire board, if you find any o change to x

    again iterate from start replace all t with o
    """
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        O = "O"
        X = "X"
        T = "T"

        def dfs(i, j):
            if (
                i < 0 or i >= rows or
                j < 0 or j >= cols or
                board[i][j] != O
            ):
                return

            board[i][j] = T

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # Mark Ts
        # Top row
        for c in range(cols):
            if board[0][c] == O:
                dfs(0, c)

        # bottom row
        for c in range(cols):
            if board[rows - 1][c] == O:
                dfs(rows - 1, c)

        # left column
        for r in range(rows):
            if board[r][0] == O:
                dfs(r, 0)

        # right column
        for r in range(rows):
            if board[r][cols - 1] == O:
                dfs(r, cols - 1)


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == O:
                    board[r][c] = X

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == T:
                    board[r][c] = O