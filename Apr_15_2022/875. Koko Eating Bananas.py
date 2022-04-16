class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = float("inf")
        while left <= right:
            mid = left + (right - left) // 2

            hours_needed = 0

            for pile in piles:
                hours_needed += math.ceil(pile / mid)

            if hours_needed <= h:
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1

        return ans
