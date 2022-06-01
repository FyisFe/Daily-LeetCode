class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        ans = [0, 0]

        for i in range(2, len(cost) + 1):
            ans.append(min(cost[i - 1] + ans[i - 1], cost[i - 2] + ans[i - 2]))

        return ans[-1]
