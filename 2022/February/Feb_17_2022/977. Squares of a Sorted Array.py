class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        right = -1
        left = -1
        res = []
        for idx in range(len(nums)):
            if nums[idx] >= 0:
                right = idx
                left = idx - 1
                break
        if right is -1:
            return [x ** 2 for x in nums][::-1]
        while right < len(nums) and left >= 0:
            if abs(nums[right]) > abs(nums[left]):
                res.append(nums[left] ** 2)
                left -= 1
            else:
                res.append(nums[right] ** 2)
                right += 1

        while right < len(nums):
            res.append(nums[right] ** 2)
            right += 1

        while left >= 0:
            res.append(nums[left] ** 2)
            left -= 1

        return res


"""Better Solution

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
	
        left,right = 0,len(nums)-1
        
        results = []
        
        while left<=right:
            
            if abs(nums[left])>abs(nums[right]):
                results.append(nums[left]**2)
                left += 1
            else:
                results.append(nums[right]**2)
                right -= 1
        
        return results[::-1]

"""
