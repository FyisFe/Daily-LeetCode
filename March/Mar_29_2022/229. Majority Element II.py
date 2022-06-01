class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1, num2, cnt1, cnt2, n = 0, 0, 0, 0, len(nums)

        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
            elif cnt1 == 0:
                num1 = num
                cnt1 = 1
            elif cnt2 == 0:
                num2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1 = 0
        cnt2 = 0
        ans = []
        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1

        if cnt1 > n // 3:
            ans.append(num1)
        if cnt2 > n // 3:
            ans.append(num2)

        return ans
