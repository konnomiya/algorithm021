class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row = click[0]
        col = click[1]
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        self.dfs(board, row, col, directions)
        return board

    def dfs(self, board, row, col, directions):
        if board[row][col] != 'E':
            return

        adjacent_mine = 0
        for delta_x, delta_y in directions:
            new_x = row + delta_x
            new_y = col + delta_y
            if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) and board[new_x][new_y] == 'M':
                adjacent_mine += 1

        if adjacent_mine != 0:
            board[row][col] = str(adjacent_mine)
            return
        else:
            board[row][col] = 'B'

        for delta_x, delta_y in directions:
            new_x = row + delta_x
            new_y = col + delta_y
            if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) and board[new_x][new_y] == 'E':
                self.dfs(board, new_x, new_y, directions)