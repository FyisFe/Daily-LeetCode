class Solution:
    def exist(self, board, word: str) -> bool:
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        que = []
        m = len(board)
        n = len(board[0])
        visited = None

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    que.append((i, j))

        if not que:
            return False
        found = False

        def helper(x, y, idx):
            nonlocal found
            if found:
                return
            visited[x][y] = True
            if idx == len(word):
                found = True
                return
            for dx, dy in direction:
                nx = dx + x
                ny = dy + y

                if (
                    nx >= 0
                    and nx < m
                    and ny >= 0
                    and ny < n
                    and visited[nx][ny] == False
                    and board[nx][ny] == word[idx]
                ):
                    helper(nx, ny, idx + 1)
            visited[x][y] = False

        for sx, sy in que:
            visited = [[False for _ in range(n)] for __ in range(m)]
            helper(sx, sy, 1)
            if found:
                return True

        return False
