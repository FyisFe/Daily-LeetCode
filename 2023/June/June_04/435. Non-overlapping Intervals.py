class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals by their end time
        intervals.sort(key=lambda x: x[1])

        # Initialize variables
        end = intervals[0][1]
        count = 1

        # Iterate over the rest of the intervals
        for i in range(1, len(intervals)):
            # If the start time of the current interval is greater than or equal to the end time of the previous interval, they don't overlap
            if intervals[i][0] >= end:
                # Update end time to be the end time of the current interval
                end = intervals[i][1]
                # Increment the count of non-overlapping intervals
                count += 1
            # If they overlap, discard the current interval
            # (we don't need to update end time or count)
            # because the previous interval has a smaller end time and a higher priority
            else:
                continue

        # The number of intervals to remove is the difference between the total number of intervals and the count of non-overlapping intervals
        return len(intervals) - count
