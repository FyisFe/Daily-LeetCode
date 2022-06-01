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
    def minCostConnectPoints(self, points) -> int:
        def manhattanDistance(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

        graph = []

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                graph.append([i, j, manhattanDistance(points[i], points[j])])

        uf = UnionFind(len(points))
        sorted_graph = sorted(graph, key=lambda x: x[2])
        cost = 0
        for edge in sorted_graph:
            if uf.count == 1:
                return cost

            if uf.find(edge[0]) != uf.find(edge[1]):
                cost += edge[2]
                uf.union(edge[0], edge[1])

        return cost
