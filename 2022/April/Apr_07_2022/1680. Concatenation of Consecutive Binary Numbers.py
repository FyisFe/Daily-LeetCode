class Solution:
    def concatenatedBinary(self, n: int) -> int:
        str = ""
        MOD = 10**9 + 7
        for i in range(1, n + 1):
            str += bin(i)[2:]

        return int(str, 2) % MOD
