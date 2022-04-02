from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        def getDistance(num1, num2):
            return abs(num1 - num2)

        ans = 0
        arr2 = sorted(arr2)
        arr2_len = len(arr2) - 1
        for num1 in arr1:
            left = 0
            right = arr2_len
            found = False
            while left <= right:
                mid = (left + right) // 2

                if getDistance(num1, arr2[mid]) <= d:
                    found = True
                    break

                if num1 > arr2[mid]:
                    left = mid + 1

                else:
                    right = mid - 1

            if not found:
                ans += 1

        return ans


sol = Solution()
sol.findTheDistanceValue([], [1, 5, 2], 1)
