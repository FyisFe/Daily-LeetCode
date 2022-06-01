class Solution:
    def getAverages(self, nums, k: int):
        ans = []
        n = len(nums)
        prev = ""
        avg_len = 2 * k + 1

        for i in range(n):
            left = i - k
            right = i + k
            if left < 0 or right >= n:
                ans.append(-1)

            else:
                if prev == "":
                    prev = sum(nums[left : right + 1])
                    ans.append(prev // avg_len)
                else:
                    prev = prev - nums[left - 1] + nums[right]
                    ans.append(prev // avg_len)

        return ans
