class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left = 1
        right = x // 2

        while left <= right:
            mid = left + (right - left) // 2
            tmp = mid ** 2
            if tmp == x:
                return mid

            if tmp > x:
                right = mid - 1

            else:
                left = mid + 1

        return left - 1
