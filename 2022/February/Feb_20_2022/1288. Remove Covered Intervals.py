class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res, end_pos = 0, 0

        sortedList = sorted(intervals, key=lambda i: (i[0], -i[1]))

        for _, end in sortedList:
            if end > end_pos:
                res += 1
                end_pos = end

        return res
