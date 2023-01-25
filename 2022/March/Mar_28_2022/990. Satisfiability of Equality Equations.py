class UnionFind:
    def __init__(self, size) -> None:
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
    def equationsPossible(self, equations) -> bool:
        hm = {}
        idx = 0

        eq_list = []
        neq_list = []

        for eq in equations:
            if not eq[0] in hm:
                hm[eq[0]] = idx
                idx += 1

            if not eq[3] in hm:
                hm[eq[3]] = idx
                idx += 1

            if eq[1] == "!":
                neq_list.append(eq)
            else:
                eq_list.append(eq)

        uf = UnionFind(len(hm))
        for eq in eq_list:
            uf.union(hm[eq[0]], hm[eq[3]])

        for eq in neq_list:
            if uf.find(hm[eq[0]]) == uf.find(hm[eq[3]]):
                return False

        return True
