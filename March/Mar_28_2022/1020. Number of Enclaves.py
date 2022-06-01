class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])

        def dfs(r, c, value):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return
            grid[r][c] = value
            dfs(r - 1, c, value)
            dfs(r + 1, c, value)
            dfs(r, c + 1, value)
            dfs(r, c - 1, value)

        for r in range(m):
            dfs(r, 0, 0)
            dfs(r, n - 1, 0)

        for c in range(n):
            dfs(0, c, 0)
            dfs(m - 1, c, 0)

        return sum([1 for r in range(m) for c in range(n) if grid[r][c] == 1])
