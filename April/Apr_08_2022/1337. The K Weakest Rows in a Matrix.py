class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def countOnes(arr):
            left = 0
            right = len(arr) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if arr[mid] == 0:
                    right = mid - 1
                else:
                    left = mid + 1

            return right

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
