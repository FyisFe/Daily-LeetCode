class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        cur = 0

        for i in nums:
            if i == 1:
                cur += 1

            else:
                ans = max(ans, cur)
                cur = 0
        ans = max(ans, cur)
        return ans
