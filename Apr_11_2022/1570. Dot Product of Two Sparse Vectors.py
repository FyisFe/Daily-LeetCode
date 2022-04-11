class SparseVector:
    def __init__(self, nums: List[int]):
        self.hm = {}
        for i in range(len(nums)):
            if nums[i]:
                self.hm[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        ans = 0
        for i in vec.hm:
            if i in self.hm:
                ans += self.hm[i] * vec.hm[i]

        return ans
