from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    islands += 1
        return islands

    def bfs(self, grid, x, y):
        queue = deque([(x, y)])
        grid[x][y] = '0'
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                new_x = x + delta_x
                new_y = y + delta_y
                if not self.is_valid(grid, new_x, new_y):
                    continue
                queue.append((new_x, new_y))
                grid[new_x][new_y] = '0'

    def is_valid(self, grid, x, y):
        m = len(grid)
        n = len(grid[0])
        return 0 <= x < m and 0 <= y < n and grid[x][y] == '1'
