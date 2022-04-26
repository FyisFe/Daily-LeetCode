class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l, r = 0, citations[-1]
        while l < r:
            m = (l + r + 1) >> 1
            cnt = sum([c >= m for c in citations])
            if cnt < m:
                r = m - 1
            else:
                l = m
        return r
