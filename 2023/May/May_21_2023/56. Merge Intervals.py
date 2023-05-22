class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = [intervals[0]]

        for interval in intervals:
            if ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(interval[1], ans[-1][1])

        return ans
