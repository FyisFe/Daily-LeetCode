class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort(reverse=True)

        ans = 0

        for num1, num2 in zip(nums1, nums2):
            ans += num1 * num2

        return ans
