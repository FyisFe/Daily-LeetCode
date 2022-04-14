class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        for num in nums:
            tmp = []
            for subset in ans:
                tmp.append(subset + [num])
            ans += tmp

        return ans
