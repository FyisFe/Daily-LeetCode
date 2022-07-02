class Solution:
    def maxArea(
        self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]
    ) -> int:

        consecutive_difference_Hori = []

        consecutive_difference_Vert = []

        horizontalCuts = sorted(horizontalCuts + [0, h])
        verticalCuts = sorted(verticalCuts + [0, w])

        for i in range(len(horizontalCuts) - 1):
            diff = horizontalCuts[i + 1] - horizontalCuts[i]
            consecutive_difference_Hori.append(diff)

        for j in range(len(verticalCuts) - 1):
            diff = verticalCuts[j + 1] - verticalCuts[j]
            consecutive_difference_Vert.append(diff)

        return (max(consecutive_difference_Hori) * max(consecutive_difference_Vert)) % (
            (10 ** 9) + 7
        )
