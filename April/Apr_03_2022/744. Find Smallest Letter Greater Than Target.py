class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[-1] <= target:
            return letters[0]
        left = 0
        right = len(letters) - 1

        while left < right:
            mid = left + (right - left) // 2

            if letters[mid] > target:
                right = mid

            else:
                left = mid + 1
        return letters[right]
