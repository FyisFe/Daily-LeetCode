class Solution:
    def summaryRanges(self, nums):
        res = []
        i = 0
        while i < len(nums):
            start = i
            end = i
            while end + 1 < len(nums) and nums[end + 1] == nums[end] + 1:
                end += 1

            if end == start:
                res.append(str(nums[end]))
            else:
                res.append(str(nums[start]) + "->" + str(nums[end]))

            i = end + 1

        return res
