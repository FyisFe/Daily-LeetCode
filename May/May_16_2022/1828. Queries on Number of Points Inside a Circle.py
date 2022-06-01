class Solution:
    def countPoints(self, points, queries):
        def getDistance(x1, y1, x2, y2):
            return (x1 - x2) ** 2 + (y1 - y2) ** 2

        def count(x, y, r):
            cnt = 0
            for point in points:
                if getDistance(point[0], point[1], x, y) <= r**2:
                    cnt += 1
            return cnt

        return [count(x, y, r) for x, y, r in queries]
