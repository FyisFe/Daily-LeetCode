class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        adjlist = [[float("inf") for __ in range(n + 1)] for _ in range(n + 1)]
        for s, e, d in times:
            adjlist[s][e] = d

        dist = [float("inf")] * (n + 1)
        dist[k] = 0
        visited = set()

        while True:
            next_node = -1
            for i in range(1, n + 1):
                if i not in visited and (next_node == -1 or dist[i] < dist[next_node]):
                    next_node = i

            if next_node == -1:
                break

            visited.add(next_node)
            for i in range(1, n + 1):
                if i not in visited and adjlist[next_node][i] != float("inf"):
                    if dist[i] > dist[next_node] + adjlist[next_node][i]:
                        dist[i] = dist[next_node] + adjlist[next_node][i]

        for i in dist[1:]:
            if i == float("inf"):
                return -1

        return max(dist[1:])
