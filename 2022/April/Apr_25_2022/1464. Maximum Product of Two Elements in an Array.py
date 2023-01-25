class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_ele = -float("inf")
        sec_max_ele = -float("inf")
        for i in nums:
            if i >= max_ele:
                sec_max_ele = max_ele
                max_ele = i
            elif i > sec_max_ele:
                sec_max_ele = i

        return (max_ele - 1) * (sec_max_ele - 1)
