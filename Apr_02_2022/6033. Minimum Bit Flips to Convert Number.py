class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        n = start ^ goal
        count = 0
        while n:
            count += 1
            n &= n - 1

        return count
