class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = {0: 1}
        ans, cur = 0, 0
        for num in nums:
            cur += num
            diff = cur - k
            if diff in hm:
                ans += hm[diff]

            if cur in hm:
                hm[cur] += 1
            else:
                hm[cur] = 1

        return ans
