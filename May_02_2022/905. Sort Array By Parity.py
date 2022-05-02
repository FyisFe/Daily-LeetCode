class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num % 2:
                ans.append(num)
            else:
                ans.insert(0, num)

        return ans
