class Solution:
    def insert(self, intervals, newInterval):
        bisect.insort_right(intervals, newInterval)

        answer = []
        # O(N)
        for i in range(len(intervals)):
            if not answer or intervals[i][0] > answer[-1][1]:
                answer.append(intervals[i])
            else:
                answer[-1][1] = max(answer[-1][1], intervals[i][1])

        return answer
