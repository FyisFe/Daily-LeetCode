class UnionFind:
    def __init__(self, n):
        self.fa = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.cnt = n

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
            self.cnt -= 1


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        uf = UnionFind(n)
        connections = sorted(connections, key=lambda x: x[2])
        print(connections)
        ans = 0
        for edge in connections:
            if uf.find(edge[0] - 1) != uf.find(edge[1] - 1):
                uf.union(edge[0] - 1, edge[1] - 1)
                ans += edge[2]

        if uf.cnt == 1:
            return ans
        return -1
