class Solution:
    def employeeFreeTime(self, schedule: "[[Interval]]") -> "[Interval]":
        # step 1. collect all intervals and sort the items by the starting time
        intervals = [s for i in schedule for s in i]
        intervals = sorted(intervals, key=lambda x: x.start)

        # step 2. merge all intervals
        merged = [intervals[0]]
        for i in intervals[1:]:
            if merged[-1].end >= i.start:
                merged[-1].end = max(merged[-1].end, i.end)
            else:
                merged.append(i)

        # step 3. find the free time (gaps between intervals)
        res = []
        for i in range(len(merged) - 1):
            res.append(Interval(merged[i].end, merged[i + 1].start))

        return res
