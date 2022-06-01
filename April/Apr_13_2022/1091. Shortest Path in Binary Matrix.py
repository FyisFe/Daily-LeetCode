class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0]:
            return -1
        direction = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        que = [(0, 0, 1)]

        while que:
            x, y, dis = que.pop(0)

            if x == n - 1 and y == n - 1:
                return dis

            for dx, dy in direction:
                nxt_x, nxt_y = x + dx, y + dy

                if (
                    nxt_x >= 0
                    and nxt_x < n
                    and nxt_y >= 0
                    and nxt_y < n
                    and grid[nxt_x][nxt_y] == 0
                ):
                    grid[nxt_x][nxt_y] = 1
                    que.append((nxt_x, nxt_y, dis + 1))
        return -1
