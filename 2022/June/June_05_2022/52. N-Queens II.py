class Solution:
    def totalNQueens(self, n: int) -> int:
        def check(board, x, y):
            d = {(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)}
            for dx, dy in d:
                a = 1
                while 0 <= x + a * dx < n and 0 <= y + a * dy < n:
                    if board[x + a * dx][y + a * dy] != 0:
                        return False
                    else:
                        a += 1
            return True

        def backtrack(board, x, used):
            if x == n:
                if used == n:
                    return 1
                else:
                    return 0
            else:
                ans = 0
                for y in range(n):
                    if check(board, x, y) == True:
                        board[x][y] = 1
                        ans += backtrack(board, x + 1, used + 1)
                        board[x][y] = 0
                return ans

        return backtrack([[0 for i in range(n)] for j in range(n)], 0, 0)
