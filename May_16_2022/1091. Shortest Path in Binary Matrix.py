class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        direction = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]

        if grid[0][0]:
            return -1
        n = len(grid)

        que = [(0, 0)]
        ans = 1

        while que:
            new_que = []
            for x, y in que:
                if x == n - 1 and y == n - 1:
                    return ans
                for dx, dy in direction:
                    nx = x + dx
                    ny = y + dy
                    if nx >= 0 and nx < n and ny >= 0 and ny < n and grid[nx][ny] == 0:
                        new_que.append((nx, ny))
                        grid[nx][ny] = 1

            que = new_que
            ans += 1

        return -1
