class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return
        n, m = len(board), len(board[0])

        def dfs(x, y):
            if x < 0 or y < 0 or x >= n or y >= m:
                return
            if board[x][y] != 'O':
                return
            board[x][y] = '*'
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        def is_border(x, y):
            if x == 0 or y == 0 or x == n - 1 or y == m - 1:
                return True
            return False

        for i in range(n):
            for j in range(m):
                if is_border(i, j) == False:
                    continue
                if board[i][j] == 'O':
                    dfs(i, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '*':
                    board[i][j] = 'O'




