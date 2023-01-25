class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        lastpos = {nums[0]: 0}
        maxsum = nums[0]
        left = -1

        for i in range(1, len(nums)):

            # Find index of item if already met
            if nums[i] in lastpos:
                left = max(left, lastpos[nums[i]])

            # Save save value's index to dictionary, as we're going from left to right
            lastpos[nums[i]] = i

            # Update the current nums[i] via prefix sum
            nums[i] += nums[i - 1]

            # So it can be nums[i] (which is prefix  sum from 0 to i)

            # Or it can be subarray sum  from nums[left: i] if duplicate met ->
            # then formula becomes  nums[i] - nums[left]
            sub_arr_sum = nums[i] - nums[left] if left != -1 else nums[i]
            maxsum = max(maxsum, sub_arr_sum)

        return maxsum
