class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [i for i in nums if i > 0]
        neg = [i for i in nums if i < 0]

        ans = []
        p_i = 0
        p_n = 0

        while p_i < len(nums) // 2 and p_n < len(nums) // 2:
            ans.append(pos[p_i])
            ans.append(neg[p_n])
            p_i += 1
            p_n += 1

        return ans
