class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i, num in enumerate(nums):
            reach = max(reach, i + num)
            if reach >= len(nums) - 1:
                return True
            if reach == i:
                return False
