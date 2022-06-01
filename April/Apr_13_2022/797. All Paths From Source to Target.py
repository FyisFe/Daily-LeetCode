class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(graph)

        def helper(idx, cur):
            nonlocal n
            nonlocal ans
            nonlocal graph
            if idx == n - 1:
                ans.append(cur + [n - 1])
                return

            for i in graph[idx]:
                helper(i, cur + [idx])

        helper(0, [])
        return ans
