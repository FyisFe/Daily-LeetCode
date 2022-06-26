class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l, r = 0, len(cardPoints) - k
        s = sum(cardPoints[r:])
        res = s
        while r < len(cardPoints):
            s += cardPoints[l] - cardPoints[r]
            l, r = l + 1, r + 1
            res = max(res, s)

        return res
