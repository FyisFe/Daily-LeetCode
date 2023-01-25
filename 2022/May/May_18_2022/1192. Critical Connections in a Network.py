class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        disc = [-1] * n
        low = [-1] * n

        network = [[] for _ in range(n)]
        for a, b in connections:
            network[a].append(b)
            network[b].append(a)

        def tarjan(prev, node, time, disc, low, network, ans):
            if disc[node] != -1:
                return disc[node]

            disc[node] = time
            low[node] = time

            for x in network[node]:
                if x != prev:
                    newLow = tarjan(node, x, time + 1, disc, low, network, ans)
                    low[node] = min(low[node], newLow)
                    if low[x] > disc[node]:
                        ans.append([x, node])

            return low[node]

        ans = []
        tarjan(0, 0, 0, disc, low, network, ans)

        return ans
