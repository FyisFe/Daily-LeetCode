class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = {}
        for node in range(len(graph)):
            if node not in visited:
                visited[node] = 0
                q = deque()
                q.append(node)
                while q:
                    curr = q.popleft()
                    for adj in graph[curr]:
                        if adj not in visited:
                            visited[adj] = visited[curr] ^ 1
                            q.append(adj)
                        elif visited[adj] == visited[curr]:
                            return False

        return True
