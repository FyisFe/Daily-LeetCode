class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        if m <= 2 or n <= 2:
            return
        direction = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]
        lst = []

        for col in range(n):
            if board[0][col] == "O":
                lst.append((0, col))
            if board[m - 1][col] == "O":
                lst.append((m - 1, col))

        for row in range(1, m - 1):
            if board[row][0] == "O":
                lst.append((row, 0))
            if board[row][n - 1] == "O":
                lst.append((row, n - 1))

        que = deque(lst)

        while que:
            x, y = que.popleft()

            for dx, dy in direction:
                nxt_x = x + dx
                nxt_y = y + dy

                if (
                    nxt_x > 0
                    and nxt_x < m - 1
                    and nxt_y > 0
                    and nxt_y < n - 1
                    and board[nxt_x][nxt_y] == "O"
                ):
                    que.append((nxt_x, nxt_y))
                    board[nxt_x][nxt_y] = "F"

        for row in range(1, m - 1):
            for col in range(1, n - 1):
                if board[row][col] == "O":
                    board[row][col] = "X"

        for row in range(1, m - 1):
            for col in range(1, n - 1):
                if board[row][col] == "F":
                    board[row][col] = "O"
