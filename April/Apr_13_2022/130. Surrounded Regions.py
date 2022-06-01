class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        dirc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        que = []
        for i in range(0, n):
            if board[0][i] == "O":
                que.append((0, i))
            if board[m - 1][i] == "O":
                que.append((m - 1, i))

        for i in range(1, m - 1):
            if board[i][0] == "O":
                que.append((i, 0))
            if board[i][n - 1] == "O":
                que.append((i, n - 1))

        while que:
            x, y = que.pop(0)
            board[x][y] = "T"
            for dx, dy in dirc:
                nx = dx + x
                ny = dy + y
                if nx >= 0 and nx < m and ny >= 0 and ny < n and board[nx][ny] == "O":
                    que.append((nx, ny))

        for i in range(m):
            for j in range(n):
                if board[i][j] != "T":
                    board[i][j] = "X"

        for i in range(m):
            for j in range(n):
                if board[i][j] == "T":
                    board[i][j] = "O"
