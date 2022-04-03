class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = 0
        j = 0
        zero_left = n
        t = m
        while i < t and j < n:
            if nums1[i] >= nums2[j]:
                for k in range(m + n - 1, i, -1):
                    nums1[k] = nums1[k - 1]
                nums1[i] = nums2[j]
                t += 1
                zero_left -= 1
                i += 1
                j += 1

            else:
                i += 1
        i = m + n - zero_left
        while i < m + n:
            nums1[i] = nums2[j]
            j += 1
            i += 1
