class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = []
        less = []
        greater = []
        for i in nums:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                greater.append(i)
            else:
                ans.append(i)

        return less + ans + greater
