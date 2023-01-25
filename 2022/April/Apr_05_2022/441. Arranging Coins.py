class Solution:
    def arrangeCoins(self, n: int) -> int:
        def getTotalNum(n):
            return n * (n + 1) // 2

        left = 0
        right = n

        while left <= right:
            mid = left + (right - left) // 2
            cur = getTotalNum(mid)

            if cur == n:
                return mid

            if n < cur:
                right = mid - 1

            else:
                left = mid + 1

        return right
