class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def countOnes(arr):
            count = 0
            for i in arr:
                if i == 1:
                    count += 1
            return count

        hm = {}
        idx = 0
        for row in mat:
            hm[idx] = countOnes(row)
            idx += 1

        sorted_hm = dict(sorted(hm.items(), key=lambda item: item[1]))

        ans = []
        idx = 0
        for key in sorted_hm:
            if idx == k:
                break
            ans.append(key)
            idx += 1

        return ans
