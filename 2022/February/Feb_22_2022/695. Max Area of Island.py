class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def getArea(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or visited[row][col]:
                return 0

            visited[row][col] = True

            if not grid[row][col]:
                return 0

            else:
                return (
                    1
                    + getArea(row + 1, col)
                    + getArea(row - 1, col)
                    + getArea(row, col + 1)
                    + getArea(row, col - 1)
                )

        m = len(grid)
        n = len(grid[0])
        visited = [[False for col in range(n)] for row in range(m)]

        max_area = 0
        for row in range(m):
            for col in range(n):
                max_area = max(getArea(row, col), max_area)

        return max_area
