class Solution:
    def shortestBridge(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        set1 = set()
        x, y, found = None, None, False
        for i in range(m):
            if found:
                break
            for j in range(n):
                if grid[i][j]:
                    x = i
                    y = j
                    found = True
                    break

        que = [(x, y)]

        while que:
            new_que = []
            for ox, oy in que:
                if (ox, oy) in set1:
                    continue
                set1.add((ox, oy))
                for dx, dy in direction:
                    nx = ox + dx
                    ny = oy + dy
                    if nx >= 0 and nx < m and ny >= 0 and ny < n and grid[nx][ny]:
                        new_que.append((nx, ny))
            que = new_que

        que = list(set1)
        visited = [[False for _ in range(n)] for __ in range(m)]
        ans = 0
        while que:
            new_que = []
            for ox, oy in que:
                if visited[ox][oy]:
                    continue
                visited[ox][oy] = True
                for dx, dy in direction:
                    nx = ox + dx
                    ny = oy + dy
                    if (
                        nx >= 0
                        and nx < m
                        and ny >= 0
                        and ny < n
                        and (nx, ny) not in set1
                    ):
                        if grid[nx][ny]:
                            return ans
                        new_que.append((nx, ny))

            que = new_que
            ans += 1
