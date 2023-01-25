class Solution:
    def minCost(
        self,
        startPos,
        homePos,
        rowCosts,
        colCosts,
    ) -> int:
        x, y = startPos
        ex, ey = homePos

        ans = 0

        if y > ey:
            for i in range(y - 1, ey - 1, -1):
                ans += colCosts[i]
        else:
            for i in range(y + 1, ey + 1):
                ans += colCosts[i]

        if x > ex:
            for i in range(x - 1, ex - 1, -1):
                ans += rowCosts[i]
        else:
            for i in range(x + 1, ex + 1):
                ans += rowCosts[i]

        return ans
