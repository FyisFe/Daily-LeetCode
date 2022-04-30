class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:

        # picture these equations as a graph

        graph = defaultdict(list)  # key: node, value: [(node, cost), ...]
        # flatten equations to graph
        for nodes, cost in zip(equations, values):
            node1, node2 = nodes
            graph[node1].append((node2, cost))
            graph[node2].append((node1, 1 / cost))

        # iterate queires and return the ans
        return [self.findPath(graph, start, end) for start, end in queries]

    def findPath(self, graph: dict, start: str, end: str) -> int:
        """calculate the cost from start to end, return -1 there is no path"""
        if start not in graph or end not in graph:
            return -1

        queue = collections.deque([(start, 1.0)])  # node, curr_cost
        visited = set([start])

        while queue:
            node, curr_cost = queue.popleft()

            if node == end:
                return curr_cost

            # explore all neighbors
            for neigh, multiple in graph[node]:
                if neigh not in visited:
                    queue.append((neigh, curr_cost * multiple))
                    visited.add(neigh)
        return -1
