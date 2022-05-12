class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, n + 1):
            if not n % i:
                factors.append(i)
            if len(factors) == k:
                return factors[-1]

        return -1
