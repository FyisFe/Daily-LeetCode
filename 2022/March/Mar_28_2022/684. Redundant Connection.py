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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        size = len(edges)
        uf = UnionFind(size)
        ans = []
        for edge in edges:
            prev_count = uf.count
            uf.union(edge[0] - 1, edge[1] - 1)
            count = uf.count

            if count == prev_count:
                ans.append(edge)

        return ans[-1]
