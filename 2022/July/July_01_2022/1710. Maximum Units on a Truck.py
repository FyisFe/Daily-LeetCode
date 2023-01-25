class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        res = 0
        for (box, unit) in boxTypes:
            if truckSize <= box:
                res += truckSize * unit
                return res
            res += box * unit
            truckSize -= box

        return res
