class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        res = {}
        result = []
        for i in sorted(set(nums)):
            res[i] = nums.count(i)

        for i in reversed(sorted(res, reverse=True, key=res.get)):
            for _ in range(nums.count(i)):
                result.append(i)

        return result
