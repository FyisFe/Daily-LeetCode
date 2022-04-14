class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(idx, cur):
            if idx > len(candidates) - 1 or sum(cur) > target:
                return

            dfs(idx + 1, cur)

            if sum(cur) + candidates[idx] == target:
                ans.append(cur + [candidates[idx]])
                return

            dfs(idx, cur + [candidates[idx]])

        dfs(0, [])
        return ans
