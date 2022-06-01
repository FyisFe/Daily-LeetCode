class UnionFind:
    def __init__(self, cnt):
        self.fa = [i for i in range(cnt)]
        self.size = [1 for _ in range(cnt)]
        self.cnt = cnt

    def find(self, x):
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x != y:
            if self.size[x] > self.size[y]:
                self.fa[y] = x
                self.size[x] += self.size[y]
            else:
                self.fa[x] = y
                self.size[y] += self.size[x]
            self.cnt -= 1


class Solution:
    def numIslands(self, grid) -> int:
        dirc = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        m = len(grid)
        n = len(grid[0])
        uf = UnionFind(m * n)
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    cnt += 1
                    for dx, dy in dirc:
                        nx = i + dx
                        ny = j + dy
                        if (
                            nx >= 0
                            and nx < m
                            and ny >= 0
                            and ny < n
                            and grid[nx][ny] == "1"
                        ):
                            print(i * n + j)
                            print(nx * n + ny)
                            uf.union(i * n + j, nx * n + ny)
        return cnt - (m * n - uf.cnt)


sol = Solution()
sol.numIslands(
    [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
)
