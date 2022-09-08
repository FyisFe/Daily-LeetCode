class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # course: prerequisites
        adj = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            course, prerequisite = pre[0], pre[1]
            adj[course].append(prerequisite)

        visited = set()

        def dfs(node):
            nonlocal visited
            for edge in adj[node]:
                if not edge in visited:
                    visited.add(edge)
                    dfs(node)

        for source in range(numCourses):
            if not source in visited and len(adj[source]) == 0:
                visited.add(source)
                dfs(source)

        return len(visited) == numCourses
