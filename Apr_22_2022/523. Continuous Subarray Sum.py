class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        sumsVisitedSoFar = set([0])
        curSum, prevSum = 0, 0
        for i, n in enumerate(nums):
            curSum += n
            curSum = curSum % k
            if i != 0 and curSum in sumsVisitedSoFar:
                return True

            sumsVisitedSoFar.add(prevSum)
            prevSum = curSum

        return False
        # TLE
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         arr_sum = sum(nums[i : j + 1])
        #         if arr_sum % k == 0:
        #             return True

        # return False


sol = Solution()
sol.checkSubarraySum([23, 2, 4, 6, 7], 6)
