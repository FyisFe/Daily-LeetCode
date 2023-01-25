class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        queue = deque([])

        for x in range(row):
            for y in range(col):
                if mat[x][y] == 0:
                    queue.append((x, y, 1))

        return self.bfs(row, col, queue, mat)

    def bfs(self, row, col, queue, grid):
        visited = set()
        while queue:
            x, y, steps = queue.popleft()

            for nx, ny in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
                if 0 <= nx < row and 0 <= ny < col and (nx, ny) not in visited:
                    if grid[nx][ny] == 1:
                        visited.add((nx, ny))
                        grid[nx][ny] = steps
                        queue.append((nx, ny, steps + 1))

        return grid
