class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dict = {}

        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        res = 0

        for key in dict:
            if dict[key] == 1:
                res += key

        return res
