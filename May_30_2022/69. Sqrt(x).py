class Solution:
    def mySqrt(self, n: int) -> int:
        eps = 1e-10
        x = 1
        while True:
            nx = (x + n / x) / 2
            if abs(x - nx) < eps:
                break
            x = nx
        return int(x)
