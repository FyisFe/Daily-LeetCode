class Solution:
    @lru_cache
    def fib(self, n: int) -> int:
        """
        F(0) = 0, F(1) = 1
        F(n) = F(n - 1) + F(n - 2), for n > 1.
        """
        if n == 0 or n == 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
