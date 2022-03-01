class Solution:
    def reverseBits(self, n: int) -> int:

        num = 0
        for i in range(32):
            num = num << 1
            bit = n % 2
            num += bit

            n = n >> 1
        return num
