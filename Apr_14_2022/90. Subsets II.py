class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        dp = [[]]
        newly_added = -1

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                tmp = []
                s = len(dp) - newly_added
                for j in range(s, len(dp)):
                    tmp.append(dp[j] + [nums[i]])
                dp += tmp
            else:
                tmp = []
                count = 0
                for x in dp:
                    tmp.append(x + [nums[i]])
                    count += 1
                dp += tmp
                newly_added = count

        return dp
