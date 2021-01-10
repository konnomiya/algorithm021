class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    before = 0
                elif i == 0:
                    before = grid[i][j - 1]
                elif j == 0:
                    before = grid[i - 1][j]
                else:
                    before = min(grid[i - 1][j], grid[i][j - 1])
                grid[i][j] = grid[i][j] + before
        return grid[m - 1][n - 1]