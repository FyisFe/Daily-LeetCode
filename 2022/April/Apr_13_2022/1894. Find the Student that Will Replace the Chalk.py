class Solution:
    def chalkReplacer(self, chalk, k: int) -> int:
        k = k % sum(chalk)
        left = 0
        right = len(chalk) - 1

        while left <= right:
            mid = left + (right - left) // 2
            res = sum(chalk[0:mid])
            if res == k:
                return mid
            if res > k:
                right = mid - 1
            if res <= k:
                left = mid + 1

        return right
