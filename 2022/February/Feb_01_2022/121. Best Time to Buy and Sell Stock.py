class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        _min = prices[0]
        profit = 0

        for i in prices:
            if i < _min:
                _min = i
            else:
                profit = max(profit, i - _min)

        return profit
