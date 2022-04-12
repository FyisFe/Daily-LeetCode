class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        i, j, m, n, ans = 0, 0, len(firstList), len(secondList), []

        while i < m and j < n:
            i_s = firstList[i][0]
            i_e = firstList[i][1]
            j_s = secondList[j][0]
            j_e = secondList[j][1]

            if i_e < j_s:
                i += 1
                continue

            if j_e < i_s:
                j += 1
                continue

            ans.append([max(i_s, j_s), min(i_e, j_e)])
            if i_e < j_e:
                i += 1
            else:
                j += 1

        return ans
