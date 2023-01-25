class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = c

        while left <= right:
            res = left ** 2 + right ** 2
            if res == c:
                return True

            if res > c:
                right -= 1
            else:
                left += 1

        return False
