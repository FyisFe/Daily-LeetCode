class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums) // 3
        hm = {}
        ans = []
        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1

        for key in hm:
            if hm[key] > threshold:
                ans.append(key)

        return ans
