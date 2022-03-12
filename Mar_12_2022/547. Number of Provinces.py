class UnionFind:
    def __init__(self, size):
        self.fa = [i for i in range(size)]
        self.size = [1 for _ in range(size)]
        self.count = size

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
                self.size[y] += self.size[x]
            else:
                self.fa[x] = y
                self.size[x] = self.size[y]
            self.count -= 1


class Solution:
    def findCircleNum(self, isConnected) -> int:
        # Union Find
        n = len(isConnected)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    uf.union(i, j)

        return uf.count
        """
        BFS:
        n = len(isConnected)
         ans = 0

         visited = [False for _ in range(n)]

         for row in range(n):
             if visited[row]:
                 continue

             ans += 1
             que = [row]

             while len(que) > 0:
                 cur_row = que.pop()
                 visited[cur_row] = True
                 for col in range(n):
                     if not visited[col] and isConnected[cur_row][col] == 1:
                         que.append(col)

         return ans

        """


sol = Solution()
sol.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
