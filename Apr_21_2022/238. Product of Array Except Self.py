class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1

        if zeros > 1:
            return [0 for _ in nums]
        ans = []

        if zeros == 1:
            all_product = 1
            for num in nums:
                if num:
                    all_product *= num
            for num in nums:
                if num:
                    ans.append(0)
                else:
                    ans.append(all_product)

        else:
            all_product = 1
            for num in nums:
                all_product *= num
            for num in nums:
                ans.append(all_product // num)

        return ans
