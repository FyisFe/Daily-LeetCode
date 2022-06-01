class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        if len(heights) == 1:
            return [0]
        curMaxHeight = [0 for _ in range(len(heights) - 1)]
        curMax = heights[-1]
        curMaxHeight[-1] = curMax
        ans = []

        for i in range(len(curMaxHeight) - 2, -1, -1):
            curMax = max(curMax, heights[i + 1])
            curMaxHeight[i] = curMax

        for i in range(len(heights) - 1):
            if heights[i] > curMaxHeight[i]:
                ans.append(i)

        ans.append(len(heights) - 1)
        return ans
