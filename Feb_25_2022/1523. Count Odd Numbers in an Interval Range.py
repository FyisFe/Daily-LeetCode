class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2:
            return (high - low) // 2 + 1
        return ceil((high - low) / 2)
