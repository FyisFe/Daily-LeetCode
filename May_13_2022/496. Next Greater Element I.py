class Solution:
    def nextGreaterElement(self, nums1, nums2):
        n = len(nums2)
        stack = []
        hm = {}
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop(-1)

            hm[nums2[i]] = -1 if not stack else stack[-1]
            stack.append(nums2[i])

        return [hm[i] for i in nums1]
