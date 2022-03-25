class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        ans = 0

        for a, b in costs:
            ans += a

        diff = [costs[i][1] - costs[i][0] for i in range(len(costs))]

        diff = sorted(diff)

        for i in range(n // 2):
            ans += diff[i]

        return ans
