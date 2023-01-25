class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        dp = [[]]
        for n in nums:
            tmp = []
            for x in dp:
                tmp.append(x + [n])
            dp += tmp
        return dp
