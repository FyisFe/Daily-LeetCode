class Solution:
    def getDistance(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def nearestValidPoint(self, x: int, y: int, points) -> int:
        min_dis = 1e10
        min_idx = -1
        for idx in range(len(points)):
            point = points[idx]
            if point[0] == x or point[1] == y:
                dis = self.getDistance(x, y, point[0], point[1])
                if dis < min_dis:
                    min_dis = dis
                    min_idx = idx

        return min_idx
