class Solution(object):
    def exist(self, board, word):

        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        def dfs(r, c, nextIndex):
            if nextIndex == len(word):
                return True
            if r < 0 or c < 0 or r > m - 1 or c > n - 1:
                return False
            if word[nextIndex] != board[r][c] or visited[r][c]:
                return False
            visited[r][c] = True

            result = (
                dfs(r - 1, c, nextIndex + 1)
                or dfs(r, c - 1, nextIndex + 1)
                or dfs(r + 1, c, nextIndex + 1)
                or dfs(r, c + 1, nextIndex + 1)
            )
            visited[r][c] = False
            return result

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True
        return False
