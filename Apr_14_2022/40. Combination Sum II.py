class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)

        ans = []

        def dfs(idx, cur):
            if idx > len(candidates) - 1 or sum(cur) > target:
                return

            if sum(cur) + candidates[idx] == target:
                ans.append(cur + [candidates[idx]])
                return

            tmp = idx
            while tmp < len(candidates) - 1 and candidates[tmp] == candidates[tmp + 1]:
                tmp += 1
            dfs(tmp + 1, cur)

            dfs(idx + 1, cur + [candidates[idx]])

        dfs(0, [])
        return ans
