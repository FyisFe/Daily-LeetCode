class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # {course: prerequisite}
        adj = {c: [] for c in range(numCourses)}
        inDegree = {}

        for pre in prerequisites:
            course, prerequisite = pre[0], pre[1]
            adj[prerequisite].append(course)
            if course in inDegree:
                inDegree[course] += 1
            else:
                inDegree[course] = 1

        que = []
        for i in range(numCourses):
            if not i in inDegree:
                que.append(i)

        ans = []
        while que:
            node = que.pop(0)
            ans.append(node)
            for edge in adj[node]:
                inDegree[edge] -= 1
                if inDegree[edge] == 0:
                    que.append(edge)
        return ans if len(ans) == numCourses else []
