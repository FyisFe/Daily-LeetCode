class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        ans = 0
        nums.sort()
        while i <= j:
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                ans = (ans + (pow(2, (j - i), 1000000007))) % 1000000007
                i += 1
        return ans
