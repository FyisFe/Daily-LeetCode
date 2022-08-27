class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm, ans = {}, []
        for num in nums1:
            hm[num] = 1

        for num in set(nums2):
            if num in hm:
                ans.append(num)

        return ans
