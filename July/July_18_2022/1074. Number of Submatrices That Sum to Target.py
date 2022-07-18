class Solution:
    def numSubmatrixSumTarget(self, M: List[List[int]], T: int) -> int:
        def subarrSum(nums, target):
            res = defaultdict(int)
            res[0] = 1
            ans, pre_sum = 0, 0

            for num in nums:
                pre_sum += num
                ans += res[pre_sum - target]
                res[pre_sum] += 1
            return ans

        rows, cols = len(M), len(M[0])
        ans = 0
        for i1 in range(rows):
            total = [0] * cols
            for i2 in range(i1, rows):
                for j in range(cols):
                    total[j] += M[i2][j]
                ans += subarrSum(total, T)
        return ans
