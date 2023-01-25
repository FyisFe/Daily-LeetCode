class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums = sorted(nums)
        med = nums[int(len(nums) / 2)]
        minMoveCount = 0
        for n in nums:
            minMoveCount += abs(n - med)
        return minMoveCount
