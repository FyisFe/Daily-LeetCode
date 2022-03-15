class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)

        que = deque([[0]])

        while que:
            lst = que.popleft()
            if lst[-1] == n - 1:
                res.append(lst)
            else:
                for elem in graph[lst[-1]]:
                    que.append(lst + [elem])

        return res
