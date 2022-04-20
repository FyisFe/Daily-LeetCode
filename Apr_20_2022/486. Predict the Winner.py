class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def solve(i, j, chance):

            if i > j:
                return 0
            if chance == 0:
                return max(nums[i] + solve(i + 1, j, 1), nums[j] + solve(i, j - 1, 1))
            else:
                return min(solve(i + 1, j, 0), solve(i, j - 1, 0))

        two = sum(nums)
        one = solve(0, len(nums) - 1, 0)
        two -= one
        return one >= two
