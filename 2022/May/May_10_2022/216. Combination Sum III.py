class Solution:
    def combinationSum3(self, k: int, n: int):
        ans = []

        def helper(cur_num, cur_sum, cur):
            if cur_num > 10 or cur_sum > n or len(cur) > k:
                return

            if cur_sum == n and len(cur) == k:
                ans.append(cur)
                return

            helper(cur_num + 1, cur_sum + cur_num, cur + [cur_num])
            helper(cur_num + 1, cur_sum, cur)

        helper(1, 0, [])

        return ans
