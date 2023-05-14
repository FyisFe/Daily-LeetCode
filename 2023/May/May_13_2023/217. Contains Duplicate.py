class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(set(nums)) < len(nums)
        hm = {}
        for num in nums:
            if num in hm:
                return False
            hm[num] = 1

        return True
