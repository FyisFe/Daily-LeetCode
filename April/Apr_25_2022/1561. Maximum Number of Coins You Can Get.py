class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)
        ans = 0
        n = len(piles) // 3
        idx = len(piles) - 2

        while n > 0:
            ans += piles[idx]
            idx -= 2
            n -= 1

        return ans
