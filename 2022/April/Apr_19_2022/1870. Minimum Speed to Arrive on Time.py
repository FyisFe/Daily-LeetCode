class Solution:
    def minSpeedOnTime(self, dist, hour: float) -> int:
        left = 1
        right = 10**7
        ans = float("inf")

        while left <= right:
            mid = left + (right - left) // 2
            hours_need = 0

            for i in range(0, len(dist) - 1):
                hours_need += math.ceil(dist[i] / mid)
            hours_need += dist[-1] / mid

            if hours_need > hour:
                left = mid + 1
            else:
                ans = min(ans, mid)
                right = mid - 1
        if ans == float("inf"):
            return -1
        return ans
