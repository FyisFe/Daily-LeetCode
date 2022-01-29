class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = 0
        for i in range(0, len(nums) - 1):
            if not nums[i] == nums[i + 1]:
                cur += 1
                nums[cur] = nums[i + 1]
        return cur + 1
