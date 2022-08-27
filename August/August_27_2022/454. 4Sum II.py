class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        # (num1 + num2) + (num3 + num4) = 0
        hm = {}
        for num1 in nums1:
            for num2 in nums2:
                res = num1 + num2
                if res in hm:
                    hm[res] += 1
                else:
                    hm[res] = 1

        ans = 0

        for num3 in nums3:
            for num4 in nums4:
                res = num3 + num4
                if -res in hm:
                    ans += hm[-res]

        return ans
