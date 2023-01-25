class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])
        ans = 0
        curArea = 0

        def dfs(fromX, fromY):
            nonlocal curArea
            for dx, dy in direction:
                toX, toY = fromX + dx, fromY + dy
                if toX >= 0 and toX < m and toY >= 0 and toY < n and grid[toX][toY]:
                    grid[toX][toY] = 0
                    curArea += 1
                    dfs(toX, toY)

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    curArea = 1
                    grid[i][j] = 0
                    dfs(i, j)
                    ans = max(curArea, ans)

        return ans
