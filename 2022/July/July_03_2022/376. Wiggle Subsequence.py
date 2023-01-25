class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        last,count=0,1
        for i in range(len(nums)-1):
            if nums[i+1]>nums[i] and last!=1:
                count+=1
                last=1
            elif nums[i+1]<nums[i] and last!=-1:
                count+=1
                last=-1
        return count