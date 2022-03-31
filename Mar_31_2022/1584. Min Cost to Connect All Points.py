class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattanDistance(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

        graph = []

        for i in range(len(points)):
            for j in range(i + 1, len(points))

