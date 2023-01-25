class Solution:
    def containsDuplicate(self, nums) -> bool:
        dict = {}
        for num in nums:
            if num in dict:
                return True
            dict[num] = 1

        return False
