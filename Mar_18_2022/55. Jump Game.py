class Solution:
    def canJump(self, nums: List[int]) -> bool:
        idx_reachable = 0

        for i in range(len(nums)):
            if i <= idx_reachable:
                idx_reachable = Math.max(idx_reachable, nums[i] + i)
            if idx_reachable >= len(nums) - 1:
                return True
        return False
