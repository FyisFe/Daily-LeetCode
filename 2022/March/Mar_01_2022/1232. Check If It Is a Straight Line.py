class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        if coordinates[1][0] == coordinates[0][0]:
            for i in range(2, len(coordinates)):
                if coordinates[i][0] != coordinates[0][0]:
                    return False
            return True

        slope = (coordinates[1][1] - coordinates[0][1]) / (
            coordinates[1][0] - coordinates[0][0]
        )

        b = coordinates[1][1] - slope * coordinates[1][0]
        for i in range(2, len(coordinates)):
            if slope * coordinates[i][0] + b != coordinates[i][1]:
                return False
        return True
