class Solution:
    def shiftGrid(self, grid, k: int):
        num_rows, num_cols = len(grid), len(grid[0])

        que = []

        for row in range(num_rows):
            for col in range(num_cols):
                que.append(grid[row][col])

        for _ in range(k):
            que.insert(0, que.pop(-1))

        grid = [[0] * num_cols for _ in range(num_rows)]

        for row in range(num_rows):
            for col in range(num_cols):
                grid[row][col] = que.pop(0)

        return grid
