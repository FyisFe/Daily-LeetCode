class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dvd = abs(dividend)
        div = abs(divisor)
        res = 0
        while dvd >= div:
            temp = div
            inc = 1
            while temp <= dvd:
                dvd -= temp
                res += inc
                inc = 2 * inc
                temp = 2 * temp
        if (dividend <= 0 and divisor > 0) or (dividend >= 0 and divisor < 0):
            res = -res
        return min(2**31 - 1, max(-(2**31), res))
