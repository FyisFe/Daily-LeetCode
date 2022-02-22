class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        count = 0
        res = 0
        for chr in columnTitle[::-1]:
            res += (ord(chr) - ord("A") + 1) * (26 ** count)
            count += 1
        return res
