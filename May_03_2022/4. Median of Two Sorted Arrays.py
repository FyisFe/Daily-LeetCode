class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        """
        len(nums1) + len(nums2) = 5 (1,2,3,4,5)
        median = 3 (idx == 2, 5 // 2)

        len(nums1) + len(nums2) = 6 (1,2,3,4,5,6)
        median = 3.5 (idx == 2,3 6 // 2 + 6// 2 -1)
        """

        p1 = 0
        p2 = 0
        n = len(nums1)
        m = len(nums2)

        if (m + n) % 2 == 0:
            while p1 < n and p2 < m:
                if p1 + p2 == (m + n) // 2 - 1:
                    ans = None
                    if nums1[p1] < nums2[p2]:
                        ans = nums1[p1]
                        p1 += 1
                        if p1 >= n:
                            ans += nums2[p2]
                            return ans / 2
                        ans += min(nums1[p1], nums2[p2])

                    else:
                        ans = nums2[p2]
                        p2 += 1
                        if p2 >= m:
                            ans += nums1[p1]
                            return ans / 2

                        ans += min(nums1[p1], nums2[p2])

                    return ans / 2

                if nums1[p1] > nums2[p2]:
                    p2 += 1
                else:
                    p1 += 1

            while p1 < n:
                if p1 + p2 == (m + n) // 2 - 1:
                    return (nums1[p1] + nums1[p1 + 1]) / 2
                p1 += 1

            while p2 < m:
                if p1 + p2 == (m + n) // 2 - 1:
                    return (nums2[p2] + nums2[p2 + 1]) / 2
                p2 += 1

        else:
            while p1 < n and p2 < m:
                if p1 + p2 == (m + n) // 2:
                    return min(nums1[p1], nums2[p2])
                if nums1[p1] > nums2[p2]:
                    p2 += 1
                else:
                    p1 += 1
            while p1 < n:
                if p1 + p2 == (m + n) // 2:
                    return nums1[p1]
                p1 += 1

            while p2 < m:
                if p1 + p2 == (m + n) // 2:
                    return nums2[p2]
                p2 += 1
