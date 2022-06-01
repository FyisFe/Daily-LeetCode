class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.hm1 = {}
        self.hm2 = {}

        for num in nums1:
            if num in self.hm1:
                self.hm1[num] += 1
            else:
                self.hm1[num] = 1

        for num in nums2:
            if num in self.hm2:
                self.hm2[num] += 1
            else:
                self.hm2[num] = 1

    def add(self, index: int, val: int) -> None:
        self.hm2[self.nums2[index]] -= 1
        self.nums2[index] += val
        if self.nums2[index] in self.hm2:
            self.hm2[self.nums2[index]] += 1
        else:
            self.hm2[self.nums2[index]] = 1

    def count(self, tot: int) -> int:
        ans = 0
        for key in self.hm1:
            if tot - key in self.hm2:
                ans += self.hm1[key] * self.hm2[tot - key]

        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)

#  hm => key, value
#  Two sum, multiply together
