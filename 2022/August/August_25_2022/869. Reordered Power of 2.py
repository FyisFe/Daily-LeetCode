class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        count = Counter(str(n))
        return any(Counter(str(1 << i)) == count for i in range(30))
